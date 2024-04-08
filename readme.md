# Installationsanleitung

## Anwendung
Diese Applikation generiert eine Leistungskruve aus einer CSV Datei

## Setup
- Repository herunterladen und entzippen
- Is Repository wechseln und ein Virtuelles Enviorment anlegen: ```python -m venv .venv```
- Virtuelles Enviorment aktivieren: ```.\.venv\Scripts\activate```
    - Sollte ein Fehler auftreten ```Set-ExecutionPolicy Unrestricted -Scope Process``` ausführen und nochmals aktivieren
- Packages mit ```pip install -r requirements.txt``` installieren
- Eine geeignete ativity.csv Datei in ```\data``` kopieren, oder die vorhandene nutzen
- In ```\source``` wechseln und ```python main.py``` ausführen und sich über die Kurve in ```\figures``` freuen :D
