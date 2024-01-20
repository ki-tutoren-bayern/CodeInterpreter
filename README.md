# CodeInterpreter by Mike Mielchen

## Überblick 

Die von Ihnen entwickelte Web-Anwendung ist ein innovatives Lehr- und Lerninstrument, speziell konzipiert für Studierende am Lehrstuhl für Systemverfahrenstechnik. Der Hauptzweck dieser Anwendung liegt darin, Studierenden, die in ihren Vorlesungen nur am Rande mit dem Programmieren in Berührung kommen, eine praktische und interaktive Erfahrung zu bieten. In diesen Vorlesungen wird häufig der Schwerpunkt auf die Vermittlung der Denkstruktur hinter dem Programmieren, also dem Pseudocode, gelegt. Unsere Anwendung baut auf diesem Konzept auf und ermöglicht es den Studierenden, ihren Pseudocode in funktionierenden Python-Code umzuwandeln. Dieser Prozess hilft ihnen nicht nur, die Syntax und Struktur von Python zu verstehen, sondern bietet auch Einblicke in die Logik und die praktische Umsetzung von Programmierkonzepten.

Durch die Integration verschiedener interaktiver Funktionen wie der Code-Generierung, der Darstellung von Syntaxbäumen und der Token-Anzeige unterstützt die Anwendung ein tiefes und umfassendes Verständnis des Programmierens. Die Studierenden können ihren eigenen Pseudocode eingeben und diesen in Python-Code umsetzen lassen, was ihnen hilft zu verstehen, wie ihre Ideen in einer realen Programmiersprache implementiert werden können. Die Visualisierung des Syntaxbaums des generierten Codes bietet einen detaillierten Einblick in die strukturelle Verarbeitung des Codes durch den Python-Interpreter, während die Anzeige der Tokens den Studierenden hilft, die grundlegenden Bausteine der Python-Syntax zu erkennen.

Darüber hinaus ermöglicht die Funktion zur Code-Ausführung den Studierenden, unmittelbares Feedback zu erhalten, indem sie sehen, wie der generierte Code in der Praxis funktioniert. Dies fördert das experimentelle Lernen und unterstützt die Studierenden dabei, ein tieferes Verständnis für die Auswirkungen ihres Codes zu entwickeln. Die Web-Anwendung ist nicht nur auf Studierende der Systemverfahrenstechnik beschränkt, sondern bietet auch Anfängern und Interessierten einen Zugang zur Welt des Programmierens.

Insgesamt dient die Anwendung als Brücke zwischen theoretischem Wissen und praktischer Anwendung. Sie ermutigt die Studierenden, über den Tellerrand hinauszuschauen und kreatives sowie problemlösendes Denken zu entwickeln. Dies ist in der modernen technischen Bildung von entscheidender Bedeutung. Mit ihrer benutzerfreundlichen und lehrreichen Plattform bietet die Anwendung eine wertvolle Ressource für alle, die ein grundlegendes Verständnis der Programmierung erlangen möchten.

## Features

Die Web-Anwendung "Code Generator" bietet eine Reihe von Schlüsselfunktionen, die speziell darauf ausgelegt sind, den Studierenden der Systemverfahrenstechnik sowie anderen Interessierten eine intuitive und lehrreiche Erfahrung im Umgang mit Programmierung zu bieten. Diese Funktionen sind so gestaltet, dass sie den Nutzern helfen, die theoretischen Konzepte des Programmierens in praktische Fertigkeiten umzusetzen. Hier sind die wichtigsten Features der Anwendung im Detail:

Code-Generierung: Eines der zentralen Merkmale der Anwendung ist die Fähigkeit, aus Benutzereingaben in Form von Pseudocode funktionsfähigen Python-Code zu generieren. Diese Funktion ermöglicht es den Nutzern, ihre theoretischen Kenntnisse in Pseudocode zu formulieren und zu sehen, wie dieser in eine tatsächliche Programmiersprache umgesetzt wird. Dies ist besonders hilfreich für diejenigen, die neu in der Welt des Programmierens sind oder ihre Fähigkeiten in der Umsetzung von Ideen in Code verbessern möchten.

Syntaxbaum-Darstellung: Zur Visualisierung der Struktur des generierten Codes bietet die Anwendung eine Darstellung des Syntaxbaums. Diese Funktion ist besonders wertvoll, da sie den Nutzern hilft, die Komplexität und den Aufbau von Code besser zu verstehen. Sie zeigt auf, wie verschiedene Elemente des Codes hierarchisch miteinander verbunden sind, was für ein tieferes Verständnis der Funktionsweise von Programmiersprachen unerlässlich ist.

Token-Anzeige: Eine weitere wichtige Funktion ist die Anzeige der Tokens des generierten Codes. Tokens sind die grundlegenden Bausteine einer Programmiersprache, wie Schlüsselwörter, Operatoren, Identifikatoren und andere Syntaxelemente. Durch die Betrachtung dieser Tokens können die Nutzer ein besseres Verständnis für die Syntax von Python entwickeln und lernen, wie der Code vom Interpreter analysiert wird.

Code-Ausführung: Die Anwendung bietet auch die Möglichkeit, den generierten Code direkt auszuführen. Dies bietet den Nutzern sofortiges Feedback zu der Funktionsweise des Codes und ermöglicht es ihnen, die Auswirkungen ihrer Programmierung in Echtzeit zu sehen. Diese Funktion ist besonders nützlich, um das Verständnis für Code-Abläufe zu fördern und zu experimentieren, wie Veränderungen im Code das Ergebnis beeinflussen können.

Benutzerfreundliche Schnittstelle: Die Anwendung verfügt über eine intuitive und benutzerfreundliche Oberfläche, die es den Nutzern erleichtert, alle Funktionen effizient zu nutzen. Der klare Aufbau und die einfache Navigation machen es auch Anfängern leicht, sich zurechtzufinden und die Anwendung effektiv für ihr Lernen zu nutzen.

Interaktive Beispielaufgaben: Um das Lernen zu unterstützen, enthält die Anwendung verschiedene Beispielaufgaben, die den Nutzern helfen, die Anwendung verschiedener Programmierkonzepte zu verstehen. Diese Beispiele dienen als Ausgangspunkt für die Nutzer, um eigene Code-Varianten zu entwickeln und zu testen.

Durch diese Features bietet die Web-Anwendung "Code Generator" eine umfassende und interaktive Plattform, die es den Studierenden ermöglicht, die theoretischen Aspekte der Programmierung in praktische Fähigkeiten umzusetzen. Sie ist ein wertvolles Werkzeug für alle, die ein tieferes Verständnis für die Programmierung entwickeln wollen, sei es als Teil ihres Studiums oder aus persönlichem Interesse.

## Vorraussetzungen

Damit die "Code Generator" Web-Anwendung effektiv genutzt werden kann, müssen einige grundlegende Voraussetzungen erfüllt sein. Diese stellen sicher, dass die Anwendung reibungslos läuft und die Nutzer die volle Funktionalität erleben können. Hier sind die wichtigsten Voraussetzungen für die Verwendung dieser Anwendung:

Python-Version: Die Anwendung ist in Python geschrieben, daher ist eine Installation von Python erforderlich. Es wird empfohlen, mindestens Python 3.8 oder eine höhere Version zu verwenden, um Kompatibilitätsprobleme zu vermeiden.

Flask Framework: Das Backend der Anwendung wird mit dem Flask-Framework entwickelt. Flask ist ein Mikro-Webframework für Python, das für seine Einfachheit und Flexibilität bekannt ist. Es muss auf dem System installiert sein, auf dem die Anwendung ausgeführt wird.

OpenAI API-Schlüssel: Da die Anwendung die OpenAI GPT-3.5-API für die Code-Generierung nutzt, ist ein gültiger API-Schlüssel erforderlich. Dieser Schlüssel muss von OpenAI bezogen und entsprechend in der Anwendung konfiguriert werden.

Graphviz-Paket: Für die Darstellung des Syntaxbaums wird das Graphviz-Paket benötigt. Dieses Paket ermöglicht die Visualisierung von Graphenstrukturen, die in diesem Fall zur Repräsentation des Syntaxbaums des generierten Codes verwendet werden.

Internetzugang: Da die Anwendung mit der OpenAI-API interagiert, ist eine stabile Internetverbindung erforderlich, um die API-Anfragen erfolgreich zu bearbeiten.

Webbrowser: Ein moderner Webbrowser wird benötigt, um auf das Frontend der Anwendung zuzugreifen. Browser wie Google Chrome, Mozilla Firefox, Safari oder Microsoft Edge sollten kompatibel sein.

Basiskenntnisse in Web-Technologien: Für die Installation und Wartung der Anwendung sind Grundkenntnisse in Web-Technologien wie HTML, CSS und JavaScript nützlich, insbesondere wenn Anpassungen oder Erweiterungen vorgenommen werden sollen.

Betriebssystem: Die Anwendung sollte auf den meisten modernen Betriebssystemen laufen, einschließlich Windows, macOS und Linux-Distributionen. Es sind keine speziellen Betriebssystemanforderungen vorhanden, solange Python und die anderen benötigten Pakete unterstützt werden.

Durch das Erfüllen dieser Voraussetzungen wird sichergestellt, dass die Nutzer die "Code Generator" Web-Anwendung optimal nutzen und ein reibungsloses, lehrreiches Erlebnis haben können.

## Installation

Die Installation der "Code Generator" Web-Anwendung ist ein geradliniger Prozess, der in mehrere Schritte unterteilt ist. Befolgen Sie diese Anleitung, um die Anwendung auf Ihrem System einzurichten:

1. Klonen des Repositories
Zunächst müssen Sie das Repository der Anwendung auf Ihr lokales System klonen. Öffnen Sie dazu Ihr Terminal oder Ihre Kommandozeile und führen Sie den folgenden Befehl aus:

bash
Copy code
git clone [URL des Repositories]
cd [Name des geklonten Verzeichnisses]
Ersetzen Sie [URL des Repositories] mit der URL des GitHub-Repositories und [Name des geklonten Verzeichnisses] mit dem Namen des Verzeichnisses, in das das Repository geklont wurde.

2. Einrichten einer Python-Umgebung
Es wird empfohlen, eine virtuelle Python-Umgebung für die Anwendung einzurichten, um Konflikte mit anderen Python-Projekten auf Ihrem System zu vermeiden. Verwenden Sie den folgenden Befehl, um eine neue virtuelle Umgebung zu erstellen:

bash
Copy code
python -m venv venv
Aktivieren Sie die virtuelle Umgebung:

Unter Windows:

bash
Copy code
.\venv\Scripts\activate
Unter Unix oder MacOS:

bash
Copy code
source venv/bin/activate
3. Installation der Abhängigkeiten
Installieren Sie alle erforderlichen Abhängigkeiten mit dem in dem Repository enthaltenen requirements.txt-File:

bash
Copy code
pip install -r requirements.txt
Dieser Befehl installiert Flask, Graphviz und alle anderen benötigten Python-Pakete.

4. Setzen des OpenAI API-Schlüssels
Setzen Sie Ihre OpenAI-API-Schlüssel als Umgebungsvariable, um die API-Anfragen zu authentifizieren:

Unter Unix-basierten Systemen:

bash
Copy code
export OPENAI_API_KEY='Ihr_API_Schlüssel'
Unter Windows:

bash
Copy code
set OPENAI_API_KEY=Ihr_API_Schlüssel
Ersetzen Sie Ihr_API_Schlüssel mit Ihrem persönlichen API-Schlüssel von OpenAI.

5. Starten des Flask-Servers
Nachdem alle Abhängigkeiten installiert und die Umgebungsvariablen gesetzt wurden, können Sie den Flask-Server starten:

bash
Copy code
flask run
Die Anwendung sollte nun auf http://127.0.0.1:5000/ laufen und über einen Webbrowser zugänglich sein.

6. Überprüfung der Installation
Öffnen Sie einen Webbrowser und navigieren Sie zu http://127.0.0.1:5000/, um die Anwendung zu testen. Sie sollten die Benutzeroberfläche der "Code Generator" Web-Anwendung sehen.

7. Zusätzliche Konfigurationen
Abhängig von Ihren spezifischen Anforderungen oder dem Einsatzgebiet der Anwendung könnten weitere Konfigurationen oder Anpassungen erforderlich sein. Dazu gehören das Einrichten einer Datenbank, das Konfigurieren von Sicherheitseinstellungen oder das Anpassen des Frontends.

Mit diesen Schritten sollte die "Code Generator" Web-Anwendung erfolgreich auf Ihrem System installiert und betriebsbereit sein. Beachten Sie, dass für die Wartung oder Erweiterung der Anwendung möglicherweise zusätzliche Schritte erforderlich sind.

#Nutzung 

Die "Code Generator" Web-Anwendung ist darauf ausgelegt, eine intuitive und benutzerfreundliche Erfahrung bei der Erstellung und Analyse von Python-Code zu bieten. Hier ist eine Anleitung zur Nutzung der verschiedenen Funktionen der Anwendung:

Start der Anwendung
Öffnen Sie einen Webbrowser und navigieren Sie zu http://127.0.0.1:5000/, um auf die Startseite der Anwendung zuzugreifen.
Eingabe und Generierung von Code
Eingabe des Pseudocodes: Im Hauptfenster der Anwendung finden Sie ein Textfeld. Geben Sie hier Ihren Pseudocode oder Ihre spezifische Anfrage für den zu generierenden Python-Code ein.

Generierung des Codes: Nachdem Sie Ihren Text eingegeben haben, klicken Sie auf den Button "Generiere Code". Die Anwendung verwendet die GPT-3.5-API, um Ihren Pseudocode in Python-Code umzuwandeln.

Anzeige und Analyse des generierten Codes
Anzeige des generierten Codes: Der generierte Python-Code wird im entsprechenden Abschnitt der Anwendung angezeigt. Sie können den Code überprüfen und gegebenenfalls für Ihre Zwecke anpassen.

Syntaxbaum-Darstellung: Für eine detaillierte Analyse können Sie den Syntaxbaum des generierten Codes einsehen. Diese Funktion hilft Ihnen, die strukturelle Zusammensetzung des Codes zu verstehen.

Token-Anzeige: Die Anwendung bietet auch die Möglichkeit, die Tokens des generierten Codes anzuzeigen. Dies ist nützlich, um die verschiedenen Elemente der Python-Syntax zu verstehen.

Ausführung des generierten Codes
Um den generierten Code auszuführen, klicken Sie auf den Button "Code ausführen". Die Anwendung führt den Code aus und zeigt das Ergebnis im Bereich "Ausführungsergebnis" an. Dies ermöglicht es Ihnen, die Funktionalität des Codes sofort zu testen und zu überprüfen.
Experimentieren und Lernen
Nutzen Sie die Beispielaufgaben und experimentieren Sie mit eigenen Code-Varianten. Dies hilft Ihnen, verschiedene Programmierkonzepte zu verstehen und Ihre Fähigkeiten in der Code-Erstellung zu verbessern.
Sicherheitshinweise
Beachten Sie, dass der generierte Code auf dem Server ausgeführt wird. Verwenden Sie die Anwendung verantwortungsbewusst und vermeiden Sie die Ausführung von Code, der potenziell unsicher oder schädlich sein könnte.
Feedback und Verbesserungen
Nutzen Sie die Möglichkeit, Feedback zu geben oder Vorschläge zur Verbesserung der Anwendung zu machen. Dies kann oft direkt über die Anwendung oder über das entsprechende GitHub-Repository erfolgen.
Durch die Nutzung dieser Funktionen können Sie die "Code Generator" Web-Anwendung effektiv für Lernzwecke einsetzen, Ihr Verständnis für Python-Programmierung verbessern und Ihre Fähigkeiten im Umgang mit Code erweitern.

## Schierheitshinweise

Die "Code Generator" Web-Anwendung bietet eine leistungsfähige Plattform zur Generierung und Ausführung von Python-Code. Es ist jedoch wichtig, beim Umgang mit dieser Funktionalität bestimmte Sicherheitsaspekte zu berücksichtigen, um sowohl die Sicherheit des Systems als auch die Integrität der Anwendung zu gewährleisten.

Ausführung von generiertem Code
Potenzielle Risiken: Die Ausführung von automatisch generiertem Code, insbesondere Code, der aus externen Eingaben stammt, kann potenzielle Risiken bergen. Es besteht die Möglichkeit, dass der generierte Code unerwünschte oder schädliche Aktionen durchführt.

Begrenzung des Funktionsumfangs: Um Sicherheitsrisiken zu minimieren, ist der Funktionsumfang des generierten Codes in der Anwendung begrenzt. Es wurden Maßnahmen implementiert, um sicherzustellen, dass nur sichere Funktionen verwendet werden können.

Sicherheitsmaßnahmen auf dem Server
Sicherheitsüberprüfungen: Das Backend der Anwendung führt Sicherheitsüberprüfungen durch, um unsichere oder potenziell gefährliche Code-Teile zu identifizieren und zu blockieren.

Ausführung in isolierter Umgebung: Der generierte Code wird in einer isolierten Umgebung ausgeführt, um das Risiko einer Beeinträchtigung des Host-Systems oder anderer Prozesse zu minimieren.

Verantwortungsvolle Nutzung
Verantwortung der Nutzer: Nutzer sollten sich der Tatsache bewusst sein, dass sie für den von ihnen eingegebenen Pseudocode verantwortlich sind. Es ist wichtig, dass Nutzer keinen Code eingeben oder ausführen, der bewusst Sicherheitslücken ausnutzt oder Schaden anrichten könnte.

Einschränkungen beachten: Nutzer sollten die Einschränkungen und Richtlinien der Anwendung beachten und keine Versuche unternehmen, diese zu umgehen.

Datenschutz und Vertraulichkeit
Vertrauliche Informationen: Vermeiden Sie die Eingabe vertraulicher oder persönlicher Informationen in die Anwendung, da der generierte Code auf einem externen Server ausgeführt wird.
Abschließender Hinweis
Diese Sicherheitshinweise dienen dazu, ein sicheres und verantwortungsvolles Erlebnis mit der "Code Generator" Web-Anwendung zu gewährleisten. Es liegt in der Verantwortung jedes Nutzers, diese Hinweise zu befolgen und die Anwendung auf eine sichere und ethische Weise zu nutzen.

# Kontakt 

Meld dich einfach irgendwie 
