# PersoSim Online-Handbuch

Quellen der PersoSim-Dokumentation. Die Dokumentation wird mit [Sphinx](https://www.sphinx-doc.org/) aus den Markdown-Dateien in `docs/source` erzeugt.

## Installationsanleitung für Windows

1. Python installieren: [python.org/downloads](https://www.python.org/downloads/) (Python install manager).

2. Eine Eingabeaufforderung (`cmd`) im Hauptverzeichnis des Projekts öffnen und die Python-Version prüfen:

   ```bat
   py --version
   ```

   Die Ausgabe muss die installierte Python-Version anzeigen, z.B. `Python 3.15.1`. Meldet die Eingabeaufforderung stattdessen, dass der Befehl `py` nicht gefunden wurde, die Eingabeaufforderung schließen und neu öffnen; sie kennt Programme, die nach ihrem Start installiert wurden, noch nicht.

   **Hinweis:** Diese Anleitung verwendet bewusst `py` statt `python`: Unter Windows startet der Befehl `python` häufig nicht Python, sondern einen Platzhalter von Windows, der nur die Meldung „Python wurde nicht gefunden; ohne Argumente ausführen, um aus dem Microsoft Store zu installieren …“ ausgibt. Wer `python` verwenden möchte, schaltet unter *Einstellungen → Apps → Erweiterte App-Einstellungen → App-Ausführungsaliase* die beiden Einträge **App-Installer** mit den Befehlen `python.exe` und `python3.exe` aus und öffnet die Eingabeaufforderung neu.

3. Python-Umgebung erstellen:

   ```bat
   py -m venv .venv
   ```

4. Python-Umgebung aktivieren:

   ```bat
   .venv\Scripts\activate.bat
   ```

   Der Pfad muss mit Backslashes angegeben werden. In der PowerShell lautet der Befehl `.venv\Scripts\Activate.ps1`; dort ist die Ausführung von Skripten standardmäßig gesperrt, daher wird die Eingabeaufforderung empfohlen.

5. Python-Abhängigkeiten installieren:

   ```bat
   cd docs
   set PYYAML_FORCE_LIBYAML=0
   pip install -r requirements.txt
   ```

   `PYYAML_FORCE_LIBYAML=0` sorgt dafür, dass PyYAML ohne seine C-Erweiterung installiert wird. Ohne diese Einstellung bricht die Installation mit Python-Versionen ab, für die PyYAML noch kein fertiges Paket anbietet (z.B. Python 3.15), weil dann Microsoft Visual C++ benötigt würde.

## Installationsanleitung für Linux (Debian/Ubuntu)

1. Python, das Modul für Python-Umgebungen und `make` installieren:

   ```bash
   sudo apt install python3 python3-venv make
   ```

2. Im Hauptverzeichnis des Projekts die Python-Umgebung erstellen und aktivieren:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Python-Abhängigkeiten installieren:

   ```bash
   cd docs
   pip install -r requirements.txt
   ```

## Installationsanleitung für macOS

1. Die Xcode Command Line Tools installieren (sie enthalten u.a. `make`). Ist bereits eine Version installiert, meldet der Befehl dies:

   ```bash
   xcode-select --install
   ```

2. Python installieren, entweder über das Installationspaket von [python.org/downloads](https://www.python.org/downloads/macos/) oder mit [Homebrew](https://brew.sh/):

   ```bash
   brew install python
   ```

   Anschließend die Version prüfen:

   ```bash
   python3 --version
   ```

3. Im Hauptverzeichnis des Projekts die Python-Umgebung erstellen und aktivieren:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Python-Abhängigkeiten installieren:

   ```bash
   cd docs
   export PYYAML_FORCE_LIBYAML=0
   pip install -r requirements.txt
   ```

   `PYYAML_FORCE_LIBYAML=0` hat dieselbe Bedeutung wie unter Windows und verhindert Abbrüche bei Python-Versionen, für die PyYAML noch kein fertiges Paket anbietet.

## PersoSim-Dokumentation bauen

Alle Befehle werden bei aktivierter Python-Umgebung im Verzeichnis `docs` ausgeführt. Nach dem Bauen befinden sich im Ordner `build` die beiden Ordner `html` und `latex`.

**Windows:** 

Am einfachsten bauen mit Hilfe von [compile.bat](./docs/compile.bat). Das Skript aktiviert die Python-Umgebung `.venv` selbst und baut HTML und LaTeX. Die HTML-Startseite öffnet [start.bat](./docs/start.bat) im Browser.

**Alle Systeme, manuell:**

```bash
sphinx-build -b html source build/html
sphinx-build -b latex source build/latex
```

**Linux und macOS, alternativ mit make:**

```bash
make html
make latex
```

Die Startseite ist `build/html/index.html` (unter Linux mit `xdg-open build/html/index.html`, unter macOS mit `open build/html/index.html` öffnen).

## PDF aus den LaTeX-Dateien generieren

Sphinx erzeugt im Ordner `build/latex` die LaTeX-Quelle `Persosim_<Version>.tex` (z.B. `Persosim_1.8.0.tex`). Daraus wird das PDF mit XeLaTeX übersetzt; XeLaTeX ist nötig, weil die Profildaten Sonderzeichen enthalten, die pdfLaTeX nicht setzen kann.

**Voraussetzung:** eine LaTeX-Distribution mit XeLaTeX und den von Sphinx verwendeten Schriften (FreeSerif, FreeSans, FreeMono). Unter Debian/Ubuntu:

```bash
sudo apt install texlive-xetex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-lang-german fonts-freefont-otf latexmk
```

Unter Windows z.B. MiKTeX, unter macOS z.B. MacTeX; in beiden Fällen müssen zusätzlich die GNU-FreeFont-Schriften installiert sein. Getestet ist der Weg unter Linux (auch unter WSL).

**PDF erzeugen:** zuerst die LaTeX-Dateien bauen (siehe oben, `sphinx-build -b latex source build/latex` bzw. `compile.bat`), dann im Ordner `build/latex`:

```bash
cd build/latex
make
```

Das von Sphinx erzeugte `Makefile` ruft XeLaTeX mehrfach auf, damit Inhaltsverzeichnis und Verweise stimmen. Alternativ erledigt `latexmk -pdfxe Persosim_<Version>.tex` dasselbe. Ohne `make` und `latexmk` (z.B. unter Windows) genügt es, `xelatex Persosim_<Version>.tex` dreimal hintereinander aufzurufen.

**Linux und macOS in einem Schritt** (Python-Umgebung aktiviert, im Verzeichnis `docs`):

```bash
make latexpdf
```

Das Ergebnis ist `build/latex/Persosim_<Version>.pdf`.

## Profildaten bearbeiten

Die Profiltabellen in `docs/source/Profiles.md` werden beim Bauen aus zwei Dateien erzeugt, und zwar für die HTML-Ausgabe als breite Vergleichstabellen mit einer Spalte je Profil und für das PDF als eine schmale Tabelle je Profil. In `Profiles.md` selbst stehen nur Platzhalter wie `{profile-table} nPA_`; sie zeigen alle Profile, deren Name mit dem angegebenen Präfix beginnt. Erzeugt werden die Tabellen von der Sphinx-Erweiterung `docs/source/_ext/profile_tables.py`.

**Profildaten:** `docs/source/_data/generated-docs/persosim-profiles.tsv`. Diese Datei entsteht beim Build von PersoSim und wird unverändert übernommen; sie wird hier nicht bearbeitet. Für eine neue PersoSim-Version die Datei aus dem Build-Ergebnis von PersoSim (`generated-docs/persosim-profiles.tsv`) über die vorhandene kopieren. Die  Sphinx-Erweiterung bereitet die Werte für die Anzeige auf:

- Datumsangaben werden als JJJJ-MM-TT angezeigt, unbekannte Teile eines Geburtsdatums als `XX` (z.B. `1994-09-XX`).
- `<absent>` wird als `(nicht vorhanden)` angezeigt: Das Profil enthält die Datengruppe nicht. Ein leeres Feld bedeutet, dass die Datengruppe ohne Inhalt vorhanden ist. Ein Feld, das bei keinem Profil einer Gruppe vorhanden ist (z.B. DG19/DG20 außerhalb der eAT-Profile), erscheint in den entsprechenden Tabellen nicht.
- Ein Leerzeichen am Anfang oder Ende eines Werts wird als `␣` angezeigt.
- Angezeigt werden die Datengruppen DG1 bis DG20; die übrigen Spalten der Datei (PIN, CAN, PUK, MRZ usw.) werden nicht verwendet.

**Beschreibungen:** `docs/source/_data/profile-notes.tsv` enthält die Spalte „Besonderheiten“ der Tabellen, eine Zeile je Profil mit den Spalten `Profil` und `Besonderheiten`, durch Tabulatoren getrennt. Diese Datei muss von Hand gepflegt werden. Kommt mit einer neuen PersoSim-Version ein Profil hinzu, wird hier eine Zeile ergänzt; fehlt die Beschreibung eines Profils, meldet der Build eine Warnung. Der Profilname steht ohne die Endung `.perso`; er muss mit `nPA_`, `eAT_`, `UB_` oder `SP_` beginnen, damit das Profil in der passenden Tabelle erscheint.

**Bearbeiten:** `profile-notes.tsv` lässt sich mit jedem Texteditor bearbeiten oder z.B. mit LibreOffice Calc öffnen (Trennzeichen „Tabulator“, Zeichensatz „UTF-8“). In Excel über *Daten → Aus Text/CSV* mit Dateiursprung „65001: Unicode (UTF-8)“ und Trennzeichen „Tabstopp“ öffnen und anschließend als *Unicode-Text (\*.txt)* unter dem Namen `profile-notes.tsv` speichern.

Nach einer Änderung an einer der beiden Dateien genügt ein erneutes Bauen (`compile.bat`, `sphinx-build` oder `make`); ein zusätzlicher Schritt ist nicht nötig.

## Hinweise für Autoren

- Die aktuelle PersoSim-Version wird ausschließlich in `docs/source/conf.py` gepflegt (`release`). Die Seiten verweisen darauf, z.B. mit `{{ release }}`; auch der Download-Link auf die GitHub-Release-Seite (`{{ release_url }}`) wird daraus gebildet.
- Das PDF heißt `Persosim_<Version>.pdf`, z.B. `Persosim_1.8.0.pdf`; der Name ergibt sich aus `release` in `conf.py`.
- Die Dokumentation selbst ist auf Deutsch; Kommentare in Code- und Konfigurationsdateien sind auf Englisch.
