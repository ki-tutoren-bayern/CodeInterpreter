# Standardbibliothek Importe
import os
import tokenize
from io import BytesIO
import re
import requests
import ast
import contextlib
import io
import token
# Drittanbieter-Bibliothek Importe
from flask import Flask, request, jsonify, render_template
import openai
#eigene Importe
from safe_functions import safe_functions

# Setzen Sie Ihren OpenAI-API-Schlüssel hier ein
openai.api_key = os.environ.get("OPENAI_API_KEY", "Standardwert")

app = Flask(__name__)

class SafeFunctionChecker(ast.NodeVisitor):
    def __init__(self, safe_functions):
        self.safe_functions = safe_functions
        self.errors = []
        self.local_defs = set()  # Zum Speichern lokaler Funktionsdefinitionen

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
        # Kombinieren aller sicherer Funktionen
        combined_safe_functions = set()
        for func_list in safe_functions.values():
            combined_safe_functions.update(func_list)

        # Parsen des Codes und Überprüfen auf unsichere Funktionen
        tree = ast.parse(code)
        checker = SafeFunctionChecker(combined_safe_functions)
        checker.visit(tree)

        return checker.errors
    except SyntaxError as e:
        return [f"Syntaxfehler im Code: {e}"]

@app.route('/display-tokens', methods=['GET'])
def display_tokens():
    try:
        # Hier geben wir die Tokens in der richtigen Form zurück
        return jsonify({'tokens': sample_tokens})
    except Exception as e:
        print(f"Fehler beim Bereitstellen der Tokens: {e}")
        return jsonify({"error": str(e)}), 500
    
@app.route('/generate-code', methods=['POST','GET'])
def generate_code():
    try:
        data = request.get_json()
        text = data['text']
        # Code zur Kommunikation mit der OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[{"role": "system", "content": "Python Code Generator"},
                      {"role": "user", "content": f"Generiere Python-Code basierend auf: {text}. Ausgabe sollte direkt in Python-Code-Form ohne zusätzliche Formatierung sein. Am Ende soll immer eine Ausgabe entstehen z.B. mit einem Befehl wie print."}]
        )
        code = response.choices[0].message['content']
        #Tokenisierung des generierten Codes
        tokens = list(tokenize.tokenize(BytesIO(code.encode('utf-8')).readline))
        # Mapping von Token-Typ-Nummern zu Token-Namen
        token_names = {value: name for name, value in vars(token).items() if isinstance(value, int)}
        # Token-Typ-Nummern durch lesbare Namen ersetzen
        token_data = [(token_names.get(tok.type, tok.type), tok.string) for tok in tokens if tok.type != tokenize.ENDMARKER]
        # Erstellen Sie den Link zum Anzeigen der Tokens
        token_url = f"http://127.0.0.1:5000/display-tokens"
        # Erstellen Sie den Link zum Anzeigen des generierten Codes
        code_url = f"http://127.0.0.1:5000/generate-code?code=true"
        # Geben Sie die Links im Terminal aus
        print(f"Um die Tokens anzuzeigen, öffnen Sie: {token_url}")
        print(f"Um den generierten Code anzuzeigen, öffnen Sie: {code_url}")
        # Zurückgeben oder Weiterverarbeiten der Tokens und des Codes
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
        print("Empfangener Code:", code) #Nur zum Debuggen. Kann später gelöscht werden ohne sorge
        # Erzeugen des Syntaxbaums aus dem Code
        syntax_tree = ast.parse(code)
        # Umwandeln des Syntaxbaums in eine String-Repräsentation (optional)
        tree_string = ast.dump(syntax_tree, indent=4)
        return jsonify({'syntax_tree': tree_string})
    
    except Exception as e:
        print(f"Fehler beim Erzeugen des Syntaxbaums: {e}")
        return jsonify({"error": str(e)}), 500
@app.route('/execute-code', methods=['POST'])
def execute_code():
    try:
        data = request.get_json()
        code = data['code']

        # Implementieren Sie hier Ihre Sicherheitsmaßnahmen
        errors = analyze_code(code, safe_functions)
        if errors:
            # Rückgabe einer Fehlermeldung an das Frontend
            return jsonify({"error": "Unsichere Funktionen gefunden: " + ", ".join(errors)})

        # Ausführung des Codes (sicherheitsbewusst)
        # Hinweis: Verwenden Sie exec() mit Vorsicht und entsprechenden Sicherheitsmaßnahmen
        # Beispiel: exec(code, {'__builtins__': {}})
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            exec(code)
        result = output.getvalue()
        # Rückgabe des Ergebnisses
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)