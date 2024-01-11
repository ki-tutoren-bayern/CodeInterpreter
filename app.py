from flask import Flask, request, jsonify, render_template
import openai
import re

#Test ob sich etwas ändert 
# Setzen Sie hier Ihren OpenAI-API-Schlüssel ein
openai.api_key = "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"

app = Flask(__name__)

@app.route('/generate-code', methods=['POST'])
def generate_code():
    try:
        data = request.get_json()  # Ändern Sie dies, um sicherzustellen, dass JSON korrekt abgerufen wird
        text = data['text']

        # Ihr Code zur Kommunikation mit der OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[{"role": "system", "content": "Python Code Generator"},
                      {"role": "user", "content": f"Schreibe Python-Code für folgendes umsetzt: {text}. Gebe nur den Code aus. Gebe keinen Befehl mit print aus."}]
        )
        code = response.choices[0].message['content']
        
        # Regex zum Extrahieren des Inhalts zwischen ```python und ```
        match = re.search(r'```python\s+(.*?)\s+```', code, re.DOTALL)
        if match:
            code_content = match.group(1)
        else:
            code_content = "Kein Code gefunden."

        # Teilen Sie den Code-Inhalt in Wörter auf
        words = code_content.split()

        # Definieren Sie eine Liste von Farben für jedes Wort (hier als Beispiel)
        # Sie können die Farben nach Ihren Wünschen anpassen
        colors = ["red", "black", "green", "black"]

        # Erstellen Sie eine HTML-Version des Codes mit Farbcodierung
        html_code = ""
        for word, color in zip(words, colors):
            html_code += f'<span style="color: {color};">{word}</span> '
        
        return jsonify({'code': html_code})
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    print("Öffnen Sie http://127.0.0.1:5000 in Ihrem Webbrowser, um das Frontend zu sehen.")
    app.run(debug=True)
