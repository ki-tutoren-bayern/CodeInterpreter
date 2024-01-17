# Sie müssen den OpenAI API Key über Ihre Systemumgebungsvariablen eintragen. Hierfür müssen Sie folgende Schritte durchführen:
  1. Öffen Sie die Windows-Suchleit, tippen Sie 'Systemumgebungsvariablen bearbeiten' ein. 
  2. Klicken Sie auf 'Umgebungsvariablen'
  3. Unter Benutzervariablen oder Systemvariablen können Sie auf 'Neu' klicken um eine neue Variablen anzulegen.
  4. Nun müsssen Sie 'OPEN_API_KEY' als Name und als Wert den tatsächlichen API-Schlüssel eingeben. 
  5. Klicken Sie auf Okay
-> Im Code steht der Codeabschnitt os.environ.get('OPENAI_API_KEY') der dann auf den API-Schlüssel zugreifen kann
