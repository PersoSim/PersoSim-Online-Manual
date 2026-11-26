# Installation
Dieses Kapitel enthält die Dateien, die für den Betrieb des Simulators nötig sind, sowie eine kurze Anleitung zur Installation. Es werden neben Windows auch Linux und macOS für die stationäre Variante von PersoSim unterstützt. Für ältere Smartphones mit NFC liegt ein Android-APK bereit.

PersoSim ist auf den 64-Bit-Betriebssystemen Windows, Linux und macOS lauffähig. 

## Systemvoraussetzungen
Java muss in Version 17 oder 21 installiert sein. Andere Versionen sind ungetestet und werden daher nicht unterstützt.

Empfohlen wird entweder:
- das Installationspaket von [Adoptium](https://adoptium.net/de/), das alle notwendigen Einstellungen automatisch vornimmt 

   oder 

- das [OpenJDK](https://jdk.java.net/), bei dem die Einstellungen manuell durchgeführt werden können. 

:::{container} logo-row
<img src="../figures/Java-logo.png" alt="Java-Logo" href="https://www.bsi.bund.de/DE/Home/home_node.html" width="35" class="logo">    
<img src="../figures/adoptium-logo.png" alt="Adoptium-Logo" href="https://www.bsi.bund.de/DE/Home/home_node.html" width="100" class="logo">    
<img src="../figures/OpenJDK_logo.png" alt="OpenJDK-Logo" href="https://www.bsi.bund.de/DE/Home/home_node.html" width="100" class="logo">
:::

<hr style="height: 2px; background: #00509B;">
<br>

## Installationsanleitung

### Installation des PersoSim-Simulators
PersoSim erfordert keine Installation im klassischen Sinne und ist nach dem Entpacken der Zip-Datei bzw. des Tar-Balls sofort lauffähig. Eine separate Installation des Editors ist seit Version 1.8 nicht mehr nötig.

Die Dateien für Windows, macOS und Linux stehen hier zum Download bereit: {{ release_url }}.

(macos-quarantine)=
:::{hint}
**Fehlermeldung unter macOS: PersoSim-Datei wird als defekt angezeigt**

Nach dem Download einer Datei unter macOS in das Standard-Verzeichnis „Downloads“ setzt macOS für diese Datei ein Quarantäne-Flag. Sobald dieses Flag gesetzt wird, kommt beim Start von PersoSim die Fehlermeldung, dass die Datei defekt sei und in den Mülleimer verschoben werden sollte. Man kann dieses Problem umgehen, indem man die PersoSim-Datei über einen anderen Weg als den Browser herunterlädt, z. B. über wget. Oder man entfernt nach dem Download das Quarantäne-Flag mit folgendem Kommando:

```bash
sudo xattr -r -d com.apple.quarantine /path/to/de.persosim.rcp.product-x.x.x-202xxxxxx-macosx.cocoa.<Architektur>.tar.gz
```
:::

### Installation des Treibers
Um den virtuellen Kartenleser (und damit die simulierten Ausweise) regulär nutzen zu können, stehen betriebssystemspezifische Treiber zur Verfügung. Diese binden PersoSim als Kartenleser im jeweiligen PC/SC-Stack ein und erlauben damit den Zugriff aus jeder kompatiblen Anwendung.
Das Vorgehen für die Installation des Treibers ist betriebssystemabhängig. Im Folgenden wird die Installation für Windows, Linux und macOS beschrieben.

#### Windows
Für die Installation von PersoSim wird lediglich als Betriebssystem Windows 10 oder neuer vorausgesetzt.
Der Treiber erkennt selbständig, um welche Version von Windows es sich handelt. Zur Installation des Treibers muss lediglich den Anweisungen des Installationsprogramms Folge geleistet werden. Im Gegensatz zu älteren Versionen des Treibers müssen keine Testzertifikate mehr separat installiert werden. Nach erfolgreicher Installation erscheint der virtuelle Kartenleser ähnlich wie physische Kartenleser als „PersoSim Virtual Reader“ im Geräte-Manager unter Smartcard-Leser und kann genutzt werden.

- Der Windows-Treiber enthält die notwendigen Dateien sowohl für Windows 10 als auch für Windows 11, jeweils für die 64-Bit-Architektur. Das Installationspaket für Windows finden Sie hier: [PersoSim_Win_Driver_x64.zip](https://persosim.github.io/software/PersoSim_Win_Driver_x64.zip)

#### Linux
Den Treiber für Linux und macOS müssen Sie derzeit selbst kompilieren. Die Sourcen finden Sie hier: [PersoSim_Driver_PCSCLite_20240917.tgz](https://persosim.github.io/software/PersoSim_Driver_PCSCLite_20240917.tgz)

Die folgende Anleitung zur Installation des Treibers unter Linux wurde für Debian 13 erstellt und dort getestet. Sie ist aber grundsätzlich auch auf anderen Linux-Derivaten durchführbar.
Zusätzlich zur Debian-13-Standardinstallation werden die folgenden Pakete benötigt:
- pcscd
- pcsc-tools
- libpcsclite-dev
- make

Diese Pakete können mit dem Befehl installiert werden: 

```bash
   sudo apt-get install pcscd pcsc-tools libpcsclite-dev make
``` 

Nach dem Entpacken des Archivs liegt der Treiber im Quellcode vor und muss zunächst kompiliert und installiert werden. Dies geschieht mit Hilfe des folgenden Aufrufs im Verzeichnis des entpackten Archivs:

```bash
   make && sudo make install
``` 

Das Laden des Treibers erfolgt mit dem Aufruf:

```bash
   sudo service pcscd restart
``` 


Analog zur Installation lässt sich der Treiber mit dem folgenden Kommando deinstallieren:

```bash
   sudo make uninstall
``` 

   
Alternativ zum virtuellen Kartenleser können Sie auch die Remote-IFD-Schnittstelle von PersoSim nutzen. Diese können Sie auch lokal einsetzen, um mit PersoSim zu kommunizieren.

#### macOS
Um die notwendige Toolchain auf macOS bereitzustellen, muss Xcode installiert werden. Zusätzlich müssen die „command line developer tools“ installiert werden. Das genaue Vorgehen hängt von der genutzten macOS- und Xcode-Version ab. Für aktuelle Versionen sollte der Konsolenbefehl zu einem Dialog für die Installation der Kommandozeilenwerkzeuge führen:

```bash
   xcode-select --install
``` 

Nach dem Entpacken des Archivs liegt der Treiber im Quellcode vor und muss zunächst kompiliert werden. Dies geschieht mit Hilfe des Aufrufs make im Verzeichnis des entpackten Archivs. Die anschließende Installation erfolgt mit dem Aufruf sudo make install. Nach einem Neustart wird der virtuelle Treiber von macOS erkannt und kann mit PersoSim genutzt werden. Die beiden Kommandos können folgendermaßen kombiniert werden:

```bash
   make && sudo make install
``` 


## Start-Anleitung

### Simulator
Die Hauptanwendung PersoSim enthält den Karten-Simulator, die Profilbearbeitung (den früheren PersoSim Editor) und den virtuellen Kartenleser, der vom Treiber an das jeweilige Betriebssystem angebunden wird.

Der Start erfolgt betriebssystemabhängig über die PersoSim.exe unter Windows bzw. PersoSim unter Linux oder macOS. Nach dem Start erscheint die Profilauswahl (siehe {numref}`fig-gui` in [](chap:sim_gui)).

Im selben Verzeichnis liegt der PersoSim Controller (PersoSimControllerc.exe unter Windows bzw. PersoSimController unter Linux und macOS), mit dem sich PersoSim fernsteuern lässt (siehe [Controller](#controler)).

Starten Sie den Simulator (Eclipse RCP) für die jeweilige Plattform (Win, macOS, Linux) im entpackten Verzeichnis. Unterstützt werden mittlerweile nur noch die Versionen mit 64 Bit!

<hr style="height: 2px; background: #00509B;">
<br>

### Android (optional)
Starten Sie die Android-Version. Das APK für Android finden Sie hier: [PersoSim_0_17_2.apk](https://persosim.github.io/software/PersoSim_0_17_2.apk)

Weitere Versionen von PersoSim finden Sie unter [Releases](https://github.com/PersoSim/PersoSim/releases) auf der GitHub-Seite.

