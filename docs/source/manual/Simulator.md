# Simulator
Im Rahmen der Entwicklung des Testwerkzeugs [GlobalTester](https://globaltester.secunet.com/de/) existiert bereits ein Simulator für elektronische Reisepässe (ePassport) bzw. den neuen elektronischen Personalausweis (nPA). Dieser Simulator wird bereits als kommerzielle Version für Konformitätstests gemäß der BSI TR-03105 erfolgreich eingesetzt. Die kommerzielle Version nutzt dabei ebenfalls nur kommerziell verfügbare Hardware, die die Kommunikation zwischen dem Kartenleser und dem Software-Simulator übernimmt. Die Hardware (Comprion CL Verify A) handelt dabei die Parameter für die Kommunikation aus und stellt dem Simulator die APDU zur Verfügung. Der Simulator wiederum berechnet die Antworten und sendet diese über die Hardware zurück an den Kartenleser. Die Abbildung zeigt diese Art der Kommunikation in Anlehnung an das ISO/OSI-Schichtenmodell (siehe {numref}`fig-schichtenmodell`).

```{figure} ../../figures/simulator_ISO_Layer.png
:alt: Header
:width: 500
:figclass: center-figure
:name: fig-schichtenmodell

: Kommunikation des Simulators veranschaulicht am Schichtenmodell ISO/OSI
```

Da für ein Open Source Projekt wie PersoSim die Hardware aufgrund der hohen Kosten nur schwer zur Verfügung steht, stellen wir hier eine Alternative bereit. Statt physischer Hardware nutzen wir hier einen virtuellen Kartenleser, der sich wie ein ganz normaler Kartenleser in bestehende Anwendungen integrieren lässt und der die Kommunikation mit dem Simulator übernimmt. In obiger Abbildung ist diese Art der Kommunikation ebenfalls abgebildet. Zusätzlich unterstützt PersoSim auch den Android Smart Card Emulator aus dem vsmartcard-Projekt (eine Emulation einer Smartcard auf einem Android-Smartphone).

Die folgende Grafik ordnet den Simulator aus dem Projekt PersoSim in den Kontext des deutschen Personalausweises und der eID-Clients sowie der eID-Server ein (siehe {numref}`fig-architecture`).

```{figure} ../../figures/persoSim_Grafik_DE.jpg
:alt: Header
:width: 700
:figclass: center-figure
:name: fig-architecture

: Zusammenspiel der Komponenten
```
