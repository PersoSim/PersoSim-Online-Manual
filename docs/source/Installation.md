# Installation
Dieses Kapitel enthält die Dateien, die für den Betrieb des Simulators nötig sind, sowie eine kurze Anleitung zur Installation. Wir unterstützen neben Windows auch Linux und macOS für die stationäre Variante von PersoSim. Für ältere Smartphones mit NFC liegt ein Android-APK bereit.

PersoSim ist auf den 64-Bit-Betriebssystemen Windows, Linux und macOS lauffähig. 

## Systemvoraussetzungen
Java muss in Version 17 oder 21 installiert sein.  

Wir empfehlen entweder:
- das Installationspaket von [Adoptium](https://adoptium.net/de/), das alle notwendigen Einstellungen automatisch vornimmt 

   oder 

- das [OpenJDK](https://jdk.java.net/), bei dem die Einstellungen manuell durchgeführt werden können. 

<img src="../figures/Java-logo.png" alt="Java-Logo" href="https://www.bsi.bund.de/DE/Home/home_node.html" width="35" class="logo">    
<img src="../figures/adoptium-logo.png" alt="Adoptium-Logo" href="https://www.bsi.bund.de/DE/Home/home_node.html" width="100" class="logo">    
<img src="../figures/OpenJDK_logo.png" alt="OpenJDK-Logo" href="https://www.bsi.bund.de/DE/Home/home_node.html" width="100" class="logo">

<hr style="height: 2px; background: #00509B;">
<br>

## Installationsanleitung

### Installation des Treibers
Um den virtuellen Kartenleser (und damit die simulierten Ausweise) regulär nutzen zu können, stehen betriebssystemspezifische Treiber zur Verfügung. Diese binden PersoSim als Kartenleser im jeweiligen PC/SC-Stack ein und erlauben damit den Zugriff aus jeder kompatiblen Anwendung.
Das Vorgehen für die Installation des Treibers ist betriebssystemabhängig. Im Folgenden wird die Installation für Windows, Linux und macOS beschrieben.

### Windows
Für die Installation von PersoSim wird lediglich als Betriebssystem Windows 10 oder neuer vorausgesetzt.
Der Treiber erkennt selbständig, um welche Version von Windows es sich handelt, und erkennt auch automatisch die Architektur (32 oder 64 Bit). Zur Installation des Treibers muss lediglich den Anweisungen des Installationsprogramms Folge geleistet werden. Im Gegensatz zu älteren Versionen des Treibers müssen keine Testzertifikate mehr separat installiert werden. Nach erfolgreicher Installation erscheint der virtuelle Kartenleser ähnlich wie physische Kartenleser als ”PersoSim Virtual Reader” im Gerätemanager unter Smartcard-Leser und kann genutzt werden.

- Der Windows-Treiber enthält die notwendigen Dateien sowohl für Windows 10 als auch für Windows 11, jeweils für die Architektur mit 32 Bit oder 64 Bit. Das Installationspaket für Windows finden Sie hier: [PersoSim_Win_Driver_x64.zip](https://persosim.github.io/software/PersoSim_Win_Driver_x64.zip)

### Linux
Den Treiber für Linux und macOS müssen Sie derzeit selbst kompilieren. Die Sourcen finden Sie hier: [PersoSim_Driver_PCSCLite_20240917.tgz](https://persosim.github.io/software/PersoSim_Driver_PCSCLite_20240917.tgz)

Die folgende Anleitung zur Installation des Treibers unter Linux wurde für Debian 13 erstellt und dort getestet. Sie ist aber grundsätzlich auch auf anderen Linux-Derivaten durchführbar.
Zusätzlich zur Debian-13-Standardinstallation werden die folgenden Pakete benötigt:
- pcscd
- pcsc-tools
- libpcsclite-dev
- make

Diese Pakete können mit dem Befehl installiert werden: 

```python
   sudo apt-get install pcscd pcsc-tools libpcsclite-dev make
``` 

Nach dem Entpacken des Archivs liegt der Treiber im Quellcode vor und muss zunächst kompiliert und installiert werden. Dies geschieht mit Hilfe des folgenden Aufrufs im Verzeichnis des entpackten Archivs:

```python
   make && sudo make install
``` 

Das Laden des Treibers erfolgt mit dem Aufruf:

```python
   sudo service pcscd restart
``` 


Analog zur Installation lässt sich der Treiber mit dem folgenden Kommando deinstallieren:

```python
   sudo make uninstall
``` 

   
Alternativ zum virtuellen Kartenleser können Sie auch die Remote-IFD-Schnittstelle von PersoSim nutzen. Diese können Sie auch lokal einsetzen, um mit PersoSim zu kommunizieren.

### macOS
Um die notwendige Toolchain auf macOS bereitzustellen, muss Xcode installiert werden. Zusätzlich müssen die ”command line developer tools” installiert werden. Das genaue Vorgehen hängt von der genutzten macOS- und Xcode-Version ab. Für aktuelle Versionen sollte der Konsolenbefehl zu einem Dialog für die Installation der Kommandozeilenwerkzeuge führen:

```python
   xcode-select --install
``` 

Nach dem Entpacken des Archivs liegt der Treiber im Quellcode vor und muss zunächst kompiliert werden. Dies geschieht mit Hilfe des Aufrufs make im Verzeichnis des entpackten Archivs. Die anschließende Installation erfolgt mit dem Aufruf sudo make install. Nach einem Neustart wird der virtuelle Treiber von macOS erkannt und kann mit PersoSim genutzt werden. Die beiden Kommandos können folgendermaßen kombiniert werden:

```python
   make && sudo make install
``` 


## Start-Anleitung

### Simulator
Die Hauptanwendung PersoSim enthält den Karten-Simulator und gleichzeitig den virtuellen Kartenleser, der vom Treiber an das jeweilige Betriebssystem angebunden wird. Die Anwendung erfordert keine Installation im klassischen Sinne. Sie ist nach dem Entpacken der Zip-Datei bzw. des Tar-Balls sofort lauffähig.

Der Start erfolgt betriebssystemabhängig über die PersoSim.exe unter Windows bzw. PersoSim unter Linux oder macOS. Nach dem Start erscheint die jeweilige GUI (siehe {numref}`fig-gui` in [](chap:sim_gui)).

Je nach Anwendungsfall (z.B. bei einer Anbindung per Remote-IFD) kann der Simulator jetzt unmittelbar genutzt werden.

Starten Sie den Simulator (Eclipse RCP) für die jeweilige Plattform (Win, macOS, Linux) im entpackten Verzeichnis. Wir unterstützen mittlerweile nur noch die Versionen mit 64 Bit!

   - Windows: [PersoSim 1.4.0](https://github.com/PersoSim/PersoSim/releases/download/1.4.0/de.persosim.rcp.product-1.4.0-20251112-win32.win32.x86_64.zip)
   - macOS: [PersoSim 1.4.0](https://github.com/PersoSim/PersoSim/releases/download/1.4.0/de.persosim.rcp.product-1.4.0-20251112-macosx.cocoa.aarch64.tar.gz)
   - Linux: [PersoSim 1.4.0](https://github.com/PersoSim/PersoSim/releases/download/1.4.0/de.persosim.rcp.product-1.4.0-20251112-linux.gtk.x86_64.tar.gz)

### Editor (optional)
Der PersoSim Editor erlaubt das Modifizieren bestehender Profile oder auch die Erzeugung völlig neuer Personalisierungen für den Simulator. Damit können Karten mit beliebigen Inhalten simuliert werden.
Die Installation des PersoSim-Editors ist keine Installation im klassischen Sinne. Installation und Start funktionieren durch Entpacken des Archivs und anschließendes Ausführen des enthaltenen Executables. Nach dem Start erscheint die GUI (siehe {numref}`fig-editor-masterfile` in [](chap:CreateNewProfil)).

<hr style="height: 2px; background: #00509B;">
<br>

Starten Sie den Editor (Eclipse RCP) für die jeweilige Plattform (Win, macOS, Linux) im entpackten Verzeichnis.

   - Windows: [PersoSim Editor 1.4.0](https://github.com/PersoSim/PersoSim/releases/download/1.4.0/de.persosim.editor.rcp.product-1.4.0-20251112-win32.win32.x86_64.zip)
   - macOS: [PersoSim Editor 1.4.0](https://github.com/PersoSim/PersoSim/releases/download/1.4.0/de.persosim.editor.rcp.product-1.4.0-20251112-macosx.cocoa.aarch64.tar.gz)
   - Linux: [PersoSim Editor 1.4.0](https://github.com/PersoSim/PersoSim/releases/download/1.4.0/de.persosim.editor.rcp.product-1.4.0-20251112-linux.gtk.x86_64.tar.gz)

### Android (optional)
Starten Sie die Android-Version. Das APK für Android finden Sie hier: [PersoSim_0_17_2.apk](https://persosim.github.io/software/PersoSim_0_17_2.apk)

Weitere Versionen von PersoSim finden Sie unter [Releases](https://github.com/PersoSim/PersoSim/releases) auf der GitHub-Seite.

