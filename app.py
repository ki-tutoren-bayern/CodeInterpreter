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
                      {"role": "user", "content": f"Generiere Python-Code basierend auf: {text}. Ausgabe sollte direkt in Python-Code-Form ohne zusätzliche Formatierung sein."}]
        )
        code = response.choices[0].message['content']
    except Exception as e:
        print(f"Fehler bei der Codegenerierung: {e}")
        return jsonify({"error": str(e)}), 500

    # Hier können Sie den generierten Code weiterverarbeiten oder direkt zurückgeben
    return jsonify({'code': code})

#Backend - Frondend Kommunikation -> Wird später zur API-Schnittstelle
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    print("Öffnen Sie http://127.0.0.1:5000 in Ihrem Webbrowser, um das Frontend zu sehen.")
    app.run(debug=True)