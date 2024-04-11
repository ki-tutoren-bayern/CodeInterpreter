import os
import tokenize
from datetime import datetime
from io import BytesIO
from multiprocessing import Process, Queue 
import ast
import contextlib
import io
import token
import time
from flask import Flask, request, jsonify, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import openai
from flask_cors import CORS
from safe_functions import safe_functions

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'static'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'Datenbank/feedback.db')

db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pseudocode_input = db.Column(db.String(500), nullable=False)
    generated_code = db.Column(db.String(500), nullable=False)
    execution_result = db.Column(db.String(500), nullable=False)
    improvement_suggestion = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='Unbearbeitet')
    comment = db.Column(db.Text, default='')

class SafeFunctionChecker(ast.NodeVisitor):
    def __init__(self, safe_functions):
        self.safe_functions = safe_functions
        self.errors = []
        self.local_defs = set()  

    def visit_FunctionDef(self, node):
        self.local_defs.add(node.name)
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
            if func_name not in self.safe_functions and func_name not in self.local_defs:
                self.errors.append(f"Unsichere Funktion verwendet: {func_name}")
        self.generic_visit(node)

def analyze_code(code, safe_functions):
    try:
        combined_safe_functions = set()
        for func_list in safe_functions.values():
            combined_safe_functions.update(func_list)
        tree = ast.parse(code)
        checker = SafeFunctionChecker(combined_safe_functions)
        checker.visit(tree)
        return checker.errors
    except SyntaxError as e:
        return [f"Syntaxfehler im Code: {e}"]
  
@app.route('/generate-code', methods=['POST','GET'])
def generate_code():
    try:
        data = request.get_json()
        text = data['text']
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[{"role": "system", "content": "Python Code Generator"},
                      {"role": "user", "content": f"Generiere Python-Code basierend auf: {text}. Ausgabe sollte direkt in Python-Code-Form ohne zusätzliche Formatierung sein. Am Ende soll immer eine Ausgabe entstehen z.B. mit einem Befehl wie print. Schreibe nur Code der direkt ausgeführt werden kann."}]
        )
        code = response.choices[0].message['content']
        tokens = list(tokenize.tokenize(BytesIO(code.encode('utf-8')).readline))
        token_names = {value: name for name, value in vars(token).items() if isinstance(value, int)}
        token_data = [(token_names.get(tok.type, tok.type), tok.string) for tok in tokens if tok.type != tokenize.ENDMARKER]
        return jsonify({'code': code, 'tokens': token_data})
    except Exception as e:
        print(f"Fehler bei der Codegenerierung: {e}")
        return jsonify({"error": str(e)}), 500
    return jsonify({'code': code})

@app.route('/generate-syntax-tree', methods=['POST'])
def generate_syntax_tree():
    try:
        data = request.get_json()
        code = data['code']
        unique_filename = 'syntax_tree_' + str(int(time.time())) + '.png'
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        image_url = url_for('static', filename=unique_filename, _external=True)
        return jsonify({'syntax_tree_image_url': image_url})
    except Exception as e:
        print(f"Fehler beim Erzeugen des Syntaxbaums: {e}")
        return jsonify({"error": str(e)}), 500

def run_code(code, output_queue):
    try:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            exec(code)
        output_queue.put(output.getvalue())
    except Exception as e:
        output_queue.put(str(e))  

@app.route('/execute-code', methods=['POST'])
def execute_code():
    try:
        data = request.get_json()
        code = data['code']
        errors = analyze_code(code, safe_functions)
        if errors:
            return jsonify({"error": "Unsichere Funktionen gefunden: " + ", ".join(errors)})
        output_queue = Queue()
        process = Process(target=run_code, args=(code, output_queue))
        process.start()
        process.join(timeout=5)
        if process.is_alive():
            process.terminate() 
            return jsonify({"error": "Zeitüberschreitung bei der Codeausführung"})
        result = output_queue.get() 
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/feedback-endpoint', methods=['POST'])
def save_feedback():
    data = request.get_json()
    feedback = Feedback(
        pseudocode_input=data['pseudocode_input'],
        generated_code=data['generated_code'],
        execution_result=data['execution_result'],
        improvement_suggestion=data['improvement_suggestion'],
        status='Unbearbeitet',
        comment=''
    )
    db.session.add(feedback)
    db.session.commit()
    return jsonify({'message': 'Feedback saved successfully'}), 200

@app.route('/feedback', methods=['GET'])
def feedback_control():
    id = request.args.get('id')
    min_id = db.session.query(db.func.min(Feedback.id)).scalar()
    max_id = db.session.query(db.func.max(Feedback.id)).scalar()
    if id is None or int(id) < min_id:
        id = max_id
    elif int(id) > max_id:
        id = min_id
    feedback = Feedback.query.get(id)
    return render_template('feedback_control.html', feedback=feedback, comment=feedback.comment)

@app.route('/update-feedback', methods=['POST'])
def update_feedback():
    id = request.args.get('id')
    feedback = Feedback.query.get(id)
    if feedback is None:
        return "Feedback not found", 404
    feedback.status = request.form.get('status')
    feedback.comment = request.form.get('comment')
    db.session.add(feedback)
    db.session.commit()
    return redirect(url_for('feedback_control'))
    
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug= True)