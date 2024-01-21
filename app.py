import os
import tokenize
from io import BytesIO
import re
import requests
import ast
import contextlib
import io
import token
import time
from flask import Flask, request, jsonify, render_template, url_for
import openai
from flask_cors import CORS
from graphviz import Digraph
from safe_functions import safe_functions

openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": ["http://localhost:8080", "https://www.moodle.tum.de/", "https://codeinterpreter.mikemielchen.com"]}})
app.config['UPLOAD_FOLDER'] = 'static'

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

def draw_ast(node, parent_name=None, graph=None):
    if graph is None:
        graph = Digraph()
        graph.attr('node', shape='box')
    name = f"node{str(id(node))}"
    label = type(node).__name__
    graph.node(name, label=label)
    if parent_name is not None:
        graph.edge(parent_name, name)
    for child in ast.iter_child_nodes(node):
        draw_ast(child, name, graph)
    return graph

@app.route('/display-tokens', methods=['GET'])
def display_tokens():
    try:
        return jsonify({'tokens': sample_tokens})
    except Exception as e:
        print(f"Fehler beim Bereitstellen der Tokens: {e}")
        return jsonify({"error": str(e)}), 500
    
@app.route('/generate-code', methods=['POST','GET'])
def generate_code():
    try:
        data = request.get_json()
        text = data['text']
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[{"role": "system", "content": "Python Code Generator"},
                      {"role": "user", "content": f"Generiere Python-Code basierend auf: {text}. Ausgabe sollte direkt in Python-Code-Form ohne zusätzliche Formatierung sein. Am Ende soll immer eine Ausgabe entstehen z.B. mit einem Befehl wie print."}]
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
        syntax_tree = ast.parse(code)
        dot = draw_ast(syntax_tree)
        unique_filename = 'syntax_tree_' + str(int(time.time()))
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        dot.render(image_path, format='png', cleanup=True)
        image_url = url_for('static', filename=unique_filename + '.png', _external=True)
        return jsonify({'syntax_tree_image_url': image_url})
    except Exception as e:
        print(f"Fehler beim Erzeugen des Syntaxbaums: {e}")
        return jsonify({"error": str(e)}), 500
    
@app.route('/execute-code', methods=['POST'])
def execute_code():
    try:
        data = request.get_json()
        code = data['code']
        errors = analyze_code(code, safe_functions)
        if errors:
            return jsonify({"error": "Unsichere Funktionen gefunden: " + ", ".join(errors)})
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            exec(code)
        result = output.getvalue()
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)