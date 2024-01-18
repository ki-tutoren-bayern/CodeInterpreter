# Standardbibliothek Importe
import os
import tokenize
from io import BytesIO
import re
import requests
import ast
import contextlib
import io
# Drittanbieter-Bibliothek Importe
from flask import Flask, request, jsonify, render_template
import openai

# Setzen Sie Ihren OpenAI-API-Schlüssel hier ein
openai.api_key = os.environ.get("OPENAI_API_KEY", "Standardwert")

app = Flask(__name__)

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
                      {"role": "user", "content": f"Generiere Python-Code basierend auf: {text}. Ausgabe sollte direkt in Python-Code-Form ohne zusätzliche Formatierung sein."}]
        )
        code = response.choices[0].message['content']

        # Tokenisierung des generierten Codes
        tokens = list(tokenize.tokenize(BytesIO(code.encode('utf-8')).readline))

        # Optional: Extrahieren der Token-Typen und -Inhalte
        token_data = [(token.type, token.string) for token in tokens]

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
    print("Öffnen Sie http://127.0.0.1:5000 in Ihrem Webbrowser, um das Frontend zu sehen.")
    app.run(debug=True)