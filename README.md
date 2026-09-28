
## Installationsanleitung für Windows

1. Python installieren: ([Link zum Herunterladen](https://www.python.org/downloads/))

2. Python-Version prüfen:
```bash
python --version
```

3. Python-Umgebung erstellen:<br>
In der Konsole den Befehl im Hauptverzeichnis des Projekts ausführen.
```bash
python -m venv .venv
```

4. Python-Umgebung aktivieren:
```bash
.venv/Scripts/activate
```

5. Navigiere zur Datei "requirements.txt": 
```bash
cd docs
```

6. Python-Abhängigkeiten installieren:
```bash
# Python-Umgebung aktivieren
pip install -r requirements.txt
```
<br>


## PersoSim-Dokumentation bauen
Die Dokumentation kann einfach und schnell über die Ausführungsdatei [compile.bat](./docs/compile.bat) gebaut werden. Nachdem die Dokumentation gebaut wurde, befinden sich im "build"-Ordner zwei Ordner "html" und "latex".

Manuell die HTML-Dateien bauen:
```bash
sphinx-build -b html source/ build/html
```

Manuell die LaTeX-Dateien bauen:
```bash
sphinx-build -b latex source/ build/latex
```
<br>


