from flask import Flask, request, jsonify, render_template
import openai
import re

#Test ob sich etwas ändert 
#OpenAI-Schlüssen entfernen bei bedarf 
openai.api_key = "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"

app = Flask(__name__)

@app.route('/generate-code', methods=['POST'])
def generate_code():
    try:
        data = request.get_json()
        text = data['text']

        # Code zur Kommunikation mit der OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[{"role": "system", "content": "Python Code Generator"},
                      {"role": "user", "content": f"Schreibe Python-Code für folgendes umsetzt: {text}. Gebe nur den Python Code aus. Dieser Code soll keine print()-Funtionen beinhalten"}]
        )
        code = response.choices[0].message['content']
        
        # Regex zum Extrahieren des Inhalts zwischen ```python und ```
        match = re.search(r'```python\s+(.*?)\s+```', code, re.DOTALL)
        if match:
            code_content = match.group(1)
        else:
            code_content = "Kein Code gefunden."

        # Teilen des Code-Inhalt in Wörtern
        words = code_content.split()

        # Definieren einer Liste von Farben für jedes Wort (hier als Beispiel)
        # Dieser Teil funktioniert noch nicht. Wenn keine Farben mehr vorhanden wird einfach abgebrochen
        colors = ["red", "black", "green", "black"]

        # Erstellen einer HTML-Version des Codes mit Farbcodierung
        #Auch hier besteht noch anpassungsbedarf 
        html_code = ""
        for word, color in zip(words, colors):
            html_code += f'<span style="color: {color};">{word}</span> '
        
        return jsonify({'code': html_code})
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify({"error": str(e)}), 500
#Backend - Frondend Kommunikation -> Wird später zur API-Schnittstelle
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    print("Öffnen Sie http://127.0.0.1:5000 in Ihrem Webbrowser, um das Frontend zu sehen.")
    app.run(debug=True)