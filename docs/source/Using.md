# PersoSim Simulator

(chap:sim_gui)= 
## Benutzeroberfläche
PersoSim führt den Anwender in drei Schritten durch die Simulation: Zuerst wird ein Profil ausgewählt (**Profile Selection**), dann die Technologie, über die die simulierte Karte bereitgestellt wird (**Technology Selection**), und schließlich wird die Simulation gestartet (**Simulation**). Der PersoSim Editor ist in die Profilauswahl integriert (siehe [Profile bearbeiten](#chap:profilesEdit)).

```{figure} ../figures/gui.png
:alt: PersoSim - Profilauswahl
:width: 600
:figclass: center-figure
:name: fig-gui

: Ausweissimulator PersoSim - Benutzeroberfläche mit der Profilauswahl
```

Das Fenster ist in drei Bereiche gegliedert (siehe {numref}`fig-gui`):

- **Kopfzeile:** der Titel des aktuellen Schritts und rechts die Schaltfläche **Info**. Sie öffnet den Dialog „About PersoSim“ mit der Versionsnummer und einem Link auf die PersoSim-Website (siehe {numref}`fig-about`).
- **Schaltflächenleiste:** **Previous** und **Next** wechseln zum vorherigen bzw. nächsten Schritt. **Logging** öffnet das Logging-Fenster (siehe [Logging-Fenster](#chap:logging)). **Start Simulation** startet die Simulation; während sie läuft, heißt die Schaltfläche **Stop Simulation**.
- **Ablaufleiste:** Die drei Punkte am unteren Rand stehen für die drei Schritte. Darunter stehen das gewählte Profil, die gewählte Technologie und der Zustand der Simulation („Simulation stopped“ bzw. „Simulation started“). Ein Klick auf einen Punkt springt direkt zum entsprechenden Schritt. Fehlt etwas oder ist eine Einstellung fehlerhaft, wird der betroffene Schritt rot markiert, bei einer Warnung gelb.

```{figure} ../figures/about.png
:alt: About PersoSim
:width: 200
:figclass: center-figure
:name: fig-about

: Dialog „About PersoSim“
```

Ist **Start Simulation** ausgegraut, nennt der Tooltip der Schaltfläche den Grund, z.B. dass kein Profil ausgewählt ist oder dass das Profil ungespeicherte Änderungen enthält. Wer die Seite **Simulation** während einer laufenden Simulation verlässt, wird gefragt, ob die Simulation beendet werden soll.

PersoSim übernimmt automatisch das helle oder dunkle Farbschema des Betriebssystems; eine Änderung der Systemeinstellung wird auch während der Laufzeit übernommen.

Die Technologie wird nicht schon beim Programmstart verbunden, sondern erst mit **Start Simulation**.


## Auswahl eines Profils
Im ersten Schritt **Profile Selection** wird das Profil (die Personalisierung) gewählt, das PersoSim simulieren soll. Im linken Bereich stehen die Quellen für Profile zur Auswahl:

- **nPA Standard Profiles:** die mitgelieferten Profile des Personalausweises.
- **eAT Standard Profiles:** die mitgelieferten Profile des elektronischen Aufenthaltstitels.
- **UB Standard Profiles:** die mitgelieferten Profile der eID-Karte für Unionsbürger.
- **Unsupported Profiles:** Sonderprofile, z.B. mit nicht zulässigen Zeichen oder eingeschränkten Protokollen.
- **Profile History:** die zehn zuletzt gewählten Profile aus allen Quellen, das neueste zuoberst.

Das gewünschte Profil wird anschließend in der Auswahlliste **Select the profile** gewählt (siehe {numref}`fig-select-profile`). Der Tooltip der Liste beschreibt kurz, wofür sich das jeweilige Profil eignet. Eine Übersicht aller mitgelieferten Profile und ihrer Daten befindet sich im Kapitel [Standardprofile](#profile).

```{figure} ../figures/select-profile.png
:alt: Auswahl eines Profils
:width: 600
:figclass: center-figure
:name: fig-select-profile

: Auswahl eines Profils in der Auswahlliste „Select the profile“
```

Mit **Profile from file** lässt sich eine beliebige Profildatei mit der Endung „.perso“ laden. Dazu öffnet PersoSim einen eigenen Dateidialog; der zuletzt verwendete Ordner wird gespeichert. Das Feld **Selected File** zeigt den vollständigen Pfad des gewählten Profils.

Im rechten Bereich **Retrieved Data** werden die Daten des gewählten Profils angezeigt. Sie lassen sich dort auch direkt bearbeiten (siehe [Profile bearbeiten](#chap:profilesEdit)). {numref}`fig-profile-eat` zeigt als Beispiel ein Profil des elektronischen Aufenthaltstitels mit den zusätzlichen Datengruppen DG19 und DG20.

```{figure} ../figures/profile-eat.png
:alt: Profil eines elektronischen Aufenthaltstitels
:width: 600
:figclass: center-figure
:name: fig-profile-eat

: Profilauswahl mit einem Profil des elektronischen Aufenthaltstitels
```

Profile lassen sich auch über die Kommandozeile laden. Hierfür wird das Kommando `loadperso` des PersoSim Controllers benutzt (siehe [Controller](#controler)). Ein so geladenes Profil zeigt PersoSim genauso an, als wäre es in der Oberfläche ausgewählt worden.


## Auswahl der Technologie
Im zweiten Schritt **Technology Selection** wird festgelegt, über welche Technologie die simulierte Karte bereitgestellt wird (siehe {numref}`fig-technology-selection`). Zur Auswahl stehen:

- **Virtual PCSC Driver:** der virtuelle Kartenleser, der über den PersoSim-Treiber in den PC/SC-Stack des Betriebssystems eingebunden wird (siehe [Installation](Installation.md)).
- **Remote IFD:** PersoSim als „Smartphone als Kartenleser“ gemäß [BSI TR-03112-6](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03112/TR-03112_node.html) (siehe [Smartphone als Kartenleser](#chap:remoteifd)).
- **VSmartcard:** Anbindung an den Android Smart Card Emulator aus dem vsmartcard-Projekt.
- **CL Verify A:** Anbindung an die Hardware Comprion CL Verify A.

Die zuletzt gewählte Technologie merkt sich PersoSim für den nächsten Programmstart.

```{figure} ../figures/technology-selection.png
:alt: Auswahl der Technologie
:width: 600
:figclass: center-figure
:name: fig-technology-selection

: Auswahl der Technologie
```

**Basis- und Standardleser:** Bei **Virtual PCSC Driver** und **Remote IFD** lässt sich zusätzlich wählen, ob PersoSim einen Basisleser (**Basic Reader**) oder einen Standardleser (**Standard Reader**) simuliert. Basisleser besitzen in der Regel weder Display noch Tastatur. Standardleser verfügen über ein Display und eine Tastatur, über die z.B. Informationen gemäß [BSI TR-03119](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03119/TR-03119_node.html) angezeigt und Passwörter eingegeben werden können. Beim Standardleser gibt der Anwender PIN, CAN oder PUK deshalb in PersoSim ein (siehe [Simulation](#chap:simulation)). Nach einem Wechsel des Lesertyps weist PersoSim darauf hin, dass der laufende Vorgang in der Anwendung, die den Leser benutzt (z.B. der AusweisApp), abgebrochen und neu gestartet werden muss, damit sie den neuen Lesertyp erkennt.

**Prüfen der Konfiguration:** Jede Technologie hat im rechten Bereich ihre Einstellungen und eine Schaltfläche **Check**. Sie prüft, ob die Voraussetzungen für die Technologie erfüllt sind, beim virtuellen Kartenleser z.B., ob der Treiber antwortet und ob der virtuelle Leser in der PC/SC-Leserliste eingetragen ist. Die Ergebnisse erscheinen für einige Sekunden mit einem grünen bzw. roten Symbol und werden zusätzlich im Log festgehalten. Dieselben Prüfungen laufen automatisch beim Klick auf **Start Simulation**. Schlägt eine Prüfung fehl, wechselt PersoSim zur Technologieauswahl, lässt die Ergebnisse stehen und markiert den Schritt in der Ablaufleiste rot (siehe {numref}`fig-technology-check-failed`).

```{figure} ../figures/technology-check-failed.png
:alt: Fehlgeschlagene Prüfung der Technologie
:width: 600
:figclass: center-figure
:name: fig-technology-check-failed

: Fehlgeschlagene Prüfung: Der virtuelle Leser ist nicht in der PC/SC-Leserliste eingetragen
```

**VSmartcard:** PersoSim zeigt einen QR-Code an, der in den Einstellungen der Android-App gescannt werden kann, um Adresse und Port zu übernehmen (siehe {numref}`fig-technology-vsmartcard`). Unter **Port** wird der Port eingestellt, unter **Interface** die Netzwerkschnittstelle, deren Adresse der QR-Code enthält. **Check** prüft, ob sich der Port öffnen lässt. PersoSim und das Android-Gerät müssen sich über das Netzwerk erreichen können.

```{figure} ../figures/technology-vsmartcard.png
:alt: Einstellungen für VSmartcard
:width: 600
:figclass: center-figure
:name: fig-technology-vsmartcard

: Einstellungen für VSmartcard (Adresse und QR-Code unkenntlich gemacht)
```

**CL Verify A:** Unter **Cl Verify connection** werden die IPv4-Adresse des CL Verify und optional der Tracing-Socket (**Open tracing socket**) eingestellt. **Check** prüft die Verbindung zum Gerät und ob sich die benötigten Ports öffnen lassen. Außerdem lassen sich der Modulationstyp (**Type A** oder **Type B**) und die maximale Bitrate von der Karte zum Lesegerät (**Maximum bit rate PICC -> PCD**) festlegen (siehe {numref}`fig-technology-clverify`).

```{figure} ../figures/technology-clverify.png
:alt: Einstellungen für CL Verify A
:width: 600
:figclass: center-figure
:name: fig-technology-clverify

: Einstellungen für CL Verify A
```


(chap:remoteifd)=
## Smartphone als Kartenleser
Die [BSI TR-03112-6](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03112/TR-03112_node.html) sieht die Funktion ”Remote-IFD” vor, auch bekannt unter dem Namen ”Smartphone als Kartenleser”. Mit dieser Funktion lässt sich ein NFC-fähiges Smartphone als Kartenleser im Kontext des Personalausweises nutzen. Auch PersoSim unterstützt diese Funktion und kann so von einem eID-Client per Netzwerk angesprochen werden.

Um diese Funktion zu nutzen, wird in der Technologieauswahl **Remote IFD** gewählt (siehe {numref}`fig-remoteifd-pairing`).

```{figure} ../figures/remoteifd-pairing.png
:alt: Aktive Kopplung bei Remote-IFD
:width: 600
:figclass: center-figure
:name: fig-remoteifd-pairing

: Remote-IFD während einer aktiven Kopplung
```

Damit ein eID-Client mit PersoSim per Remote-IFD kommunizieren kann, müssen die beiden Programme miteinander gekoppelt werden:

- **Pairing PIN:** der vierstellige Kopplungscode, voreingestellt auf ‚1234‘. Er lässt sich direkt eingeben oder mit den Pfeiltasten ändern.
- **Start pairing:** startet den Kopplungsvorgang. Während der Kopplung zeigt PersoSim den Kopplungscode an („Pairing is active with PIN: …“), die Schaltfläche heißt **Stop pairing**, und der IFD-Name lässt sich nicht ändern (siehe {numref}`fig-remoteifd-pairing`). Mit diesem Kopplungscode kann sich der eID-Client dann mit PersoSim verbinden (siehe hierzu auch die Dokumentation des eID-Clients). Nach einer erfolgreichen Kopplung erfolgt die gegenseitige Authentisierung zertifikatsbasiert, sodass keine weitere Kopplung mehr notwendig ist.
- **Gekoppelte Geräte:** Die Tabelle im oberen Bereich listet die bereits gekoppelten Anwendungen mit Namen und Zertifikat (siehe {numref}`fig-configurationRemoteIFD`). Über das Papierkorb-Symbol oder das Kontextmenü (**Delete certificate**) lässt sich eine Kopplung wieder entfernen.
- **IFD name:** der Name dieser PersoSim-Instanz. Er wird von eID-Clients zur Kopplung und zum Wiederverbinden genutzt, damit der Benutzer die entsprechende Gegenstelle auswählen kann. Der Name darf nicht leer sein.

```{figure} ../figures/configurationRemoteIFD.png
:alt: Remote-IFD mit gekoppeltem Gerät
:width: 600
:figclass: center-figure
:name: fig-configurationRemoteIFD

: Remote-IFD mit einem gekoppelten Gerät (AusweisApp) und dem Ergebnis der Prüfung (Seriennummer und Netzwerkadressen unkenntlich gemacht)
```

**Check** prüft, ob mindestens ein Gerät gekoppelt ist und ob es eine Netzwerkschnittstelle gibt, über die PersoSim den Leser im Netzwerk ankündigen kann. Ob der eID-Client im selben Netz liegt und eine Firewall die Kommunikation zulässt (UDP-Port 24727), kann PersoSim nicht prüfen.


(chap:simulation)=
## Simulation
Im dritten Schritt **Simulation** wird die Simulation mit **Start Simulation** gestartet und mit **Stop Simulation** beendet (siehe {numref}`fig-simulation`). Der Start entspricht dem Auflegen eines Ausweises auf einen Kartenleser. Beim Start prüft PersoSim das Profil und die Technologie, lädt das gewählte Profil und verbindet die Technologie. Erst wenn die Simulation läuft, steht in der Ablaufleiste „Simulation started“.

```{figure} ../figures/simulation-running.png
:alt: Laufende Simulation
:width: 600
:figclass: center-figure
:name: fig-simulation

: Laufende Simulation
```

Im rechten Bereich zeigt **Retrieved Data** die Daten des simulierten Profils. Hier lassen sich die Daten nicht bearbeiten.

**Reader Input:** Dieser Bereich ist nur beim Standardleser aktiv und dient als Ersatz für ein klassisches PinPad eines Kartenlesers:

- Oben steht die Aufforderung des Lesers, z.B. „Enter PIN“.
- In der Auswahlliste links wird die Art des Passworts gewählt (PIN, CAN oder PUK). Fordert der Leser ein Passwort an, stellt PersoSim die Art automatisch ein.
- Im Eingabefeld wird das Passwort eingegeben und mit **OK** bestätigt. Über den Pfeil neben dem Feld lassen sich die letzten fünf eingegebenen Werte der jeweiligen Art erneut auswählen.
- Ist **Automatic Input** angehakt, beantwortet PersoSim Anfragen nach PIN, CAN oder PUK automatisch mit dem zuletzt eingetragenen Wert. Die Option lässt sich auch während der Simulation umschalten. Anfragen nach einer neuen PIN (PIN-Änderung) beantwortet PersoSim nie automatisch.
- Unterhalb der Eingabe wird der CHAT der laufenden Authentisierung angezeigt. Verweilt man mit der Maus darüber, werden die angefragten Zugriffsrechte menschenlesbar aufgeschlüsselt.

Wartet der Leser auf ein Passwort, wird der Schritt in der Ablaufleiste gelb markiert und das Eingabefeld blinkt kurzzeitg.

**Credential Status:** Dieser Bereich zeigt die Fehlbedienungszähler: für die PIN die verbleibenden Versuche (**Retries left**), für die PUK den Entsperrzähler (**Reset Counter**). Vor dem Start stehen hier die Werte des Profils, während der Simulation die aktuellen Werte der simulierten Karte. Erreicht der Entsperrzähler der PUK den Wert 0, weist PersoSim einmalig darauf hin, dass die PIN nicht mehr entsperrt werden kann.


(chap:logging)=
## Logging-Fenster
Die Schaltfläche **Logging** öffnet das Fenster „PersoSim Log“, in dem Log-Informationen über sämtliche Kommandos an den Simulator sowie dessen Rückmeldungen protokolliert werden (siehe {numref}`fig-logging`). Das Fenster lässt sich unabhängig vom Hauptfenster verschieben und in der Größe ändern. Die Tabelle zeigt für jeden Eintrag Zeitstempel, Log-Level, Log-Tags und Meldung, farblich nach Log-Level unterschieden. Solange ein Eintrag markiert ist, scrollt die Ansicht nicht automatisch weiter.

```{figure} ../figures/logging.png
:alt: Logging-Fenster
:width: 600
:figclass: center-figure
:name: fig-logging

: PersoSim mit Logging-Daten
```

Über das Kontextmenü (Rechtsklick in die Tabelle) stehen folgende Funktionen zur Verfügung (siehe {numref}`fig-logging-menu`):

- **Copy selected entries:** kopiert die markierten Einträge in die Zwischenablage.
- **Configure Log Levels & Tags:** legt fest, welche Log-Level und Log-Tags angezeigt werden.
- **Load Profile from file:** lädt eine Profildatei. Sie wird anschließend auch in der Profilauswahl als gewähltes Profil angezeigt.
- **Save log to file:** speichert den Log-Inhalt in eine Datei. PersoSim fragt dabei nach dem Speicherort.
- **MultiLine log:** zeigt mehrzeilige Meldungen vollständig an.
- **Columns visibility:** blendet einzelne Spalten ein oder aus.

```{figure} ../figures/logging-menu.png
:alt: Kontextmenü des Logging-Fensters
:width: 600
:figclass: center-figure
:name: fig-logging-menu

: Kontextmenü des Logging-Fensters
```

