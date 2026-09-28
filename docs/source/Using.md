# PersoSim Simulator Handbuch

## Benutzung des PersoSim Simulators

(chap:sim_gui)= 
### Benutzeroberfläche
PersoSim stellt im Vordergrund die Benutzeroberfläche des eingebundenen virtuellen Kartenlesers dar (siehe {numref}`fig-gui`). Alle weiteren Funktionen sind über Tabs und Menüs erreichbar und werden nachfolgend erläutert.

```{figure} ../figures/gui.png
:alt: Header
:width: 300
:figclass: center-figure
:name: fig-gui

: Ausweissimulator PersoSim - GUI
```

### Laden von Personalisierungen
Personalisierungen innerhalb von PersoSim lassen sich sowohl über die Kommandozeile als auch mit Hilfe von Menüpunkten über die grafische Benutzeroberfläche laden. Dabei ist Profil 1 (Erika Mustermann) standardmäßig vorausgewählt. Nach dem Laden einer Personalisierung ist diese sofort aktiviert. Dies entspricht dem Auflegen eines Ausweises auf einen Hardware-Kartenleser. Es stehen diverse vorgefertigte Standardprofile zur Auswahl. Hierbei handelt es sich z.B. um Personalausweise sowie Unionsbürgerkarten. Eine aktuelle Übersicht der verschiedenen Personalisierungen und der darin verwendeten Daten befindet sich im Kapitel [Profile](#profile).

**Laden von Personalisierungen über das Menü:** Die wohl komfortabelste Möglichkeit, Personalisierungen zu laden, ist das Anwendungsmenü (siehe {numref}`fig-load-personalization`). Der Menüpunkt ”Personalization” bietet hierfür folgende Unterpunkte:

- **Select Perso from file:** Öffnet einen Datei-Dialog und erlaubt die Auswahl einer beliebigen Personalisierung aus einer vorliegenden XML-Datei mit der Endung ".perso".
- **Select predefined Perso template:** Erlaubt die direkte Auswahl der oben beschriebenen Standardprofile.
- **Remove card:** „entfernt“ die simulierte Karte vom Leser.

```{figure} ../figures/load-personalization.png
:alt: Header
:width: 300
:figclass: center-figure
:name: fig-load-personalization

: Ausweissimulator PersoSim - Laden eines Profils
```

**Laden von Personalisierungen über die Kommandozeile:** Auch auf der Kommandozeile lassen sich Personalisierungen einfach laden. Hierfür wird das Kommando loadperso<Dateiname> benutzt. Alternativ kann statt des Dateinamens auch eine Zahl angegeben werden, die als Abkürzung zu einem der angebotenen Standardprofile dient. Mehr Informationen zur Steuerung über die Kommandozeile finden sie hier [Controller](#controler).


### Wechseln des Lesertyps
Der virtuelle Kartenleser, der im Rahmen von PersoSim genutzt werden kann, kann so konfiguriert werden, dass er entweder einen Basis- oder einen Standardleser simuliert. Die Auswahl des Lesertyps erfolgt über den Menüpunkt ”Reader Type” (siehe {numref}`fig-simulator-interface`).

```{figure} ../figures/simulator-interface.png
:alt: Header
:width: 300
:figclass: center-figure
:name: fig-simulator-interface

: Ausweissimulator PersoSim - Einstellen des Lesertyps
```

**Basisleser** besitzen in der Regel weder Display noch Tastatur. Dementsprechend verfügt
auch der PersoSim-Basisleser lediglich über die beiden Infofelder im oberen Bereich, die anzeigen, ob eine Karte simuliert und über welche Verbindung die Simulation bereitgestellt wird (siehe {numref}`fig-basisReader`).

```{figure} ../figures/basicReader.png
:alt: Header
:width: 300
:figclass: center-figure
:name: fig-basisReader

: PersoSim als Basisleser
```
<br>

Standardleser verfügen über ein Display und eine Tastatur, über die z.B. Informationen gemäß BSI TR-03119 angezeigt und Passwörter eingegeben werden können. Entsprechend verfügt der PersoSim-Standardleser über ein Display, in dem Anweisungen und die eingegebene PIN angezeigt werden, sowie über ein Tastenfeld zur Eingabe der PIN. Unterhalb des Displays wird der zur Authentisierung übertragene CHAT angezeigt (wenn man mit der Maus darüber verweilt, werden die einzelnen Bits menschenlesbar aufgeschlüsselt).

Zusätzlich erlaubt es der PersoSim-Standardleser im rechten Bereich häufig genutzte Passwörter zu speichern und per Doppelklick direkt zu nutzen. Gerade bei der Durchführung von mehreren Tests kann die Eingabe eines Passworts (PIN, CAN oder PUK) relativ zeitaufwendig werden. Aus diesem Grund gibt es die Möglichkeit, beliebige Ziffernfolgen als Passwörter vorab zu definieren. {numref}`fig-basisReader2` zeigt diese Funktion exemplarisch: Hier sind als Passwörter sowohl ’123456’ (voreingestellte PIN für PersoSim-Profile) als auch ’500540’ (voreingestellte CAN für PersoSim-Profile) hinterlegt. Die voreingestellte PUK ‘9876543210‘ könnte ebenfalls dort angegeben werden. Nach einem Rechtsklick auf „Passwords“ im rechten Bereich können Passwörter hinzugefügt, editiert oder gelöscht werden. Bei der Verwendung von PersoSim kann anschließend je nach Kontext das entsprechende Passwort per Doppelklick ausgewählt werden. Zur weiteren Vereinfachung dient die Aktivierung des automatischen Logins (AutoLogin). Wird diese Option nach Auswahl eines Passworts angehakt, wird dieses Passwort immer verwendet und muss nicht mehr per Doppelklick ausgewählt werden.

```{figure} ../figures/basicReader2.png
:alt: Header
:width: 350
:figclass: center-figure
:name: fig-basisReader2

: PersoSim als Standardleser
```

Beim ersten Programmstart wird automatisch der Standardleser aktiviert.

Es gilt zu beachten, dass die Eingabeelemente auf dem PinPad des Standardlesers nur dann und solange aktiviert sind wie sie im Rahmen einer Kommunikation mit dem simulierten Ausweis benötigt werden. D.h. zu Programmstart sind diese zunächst ohne Funktion. Sobald eine Eingabe erforderlich ist, erscheint ein entsprechender Hinweis auf dem Display.


### Ansicht Logging und Konsole
Über den Tab ”Logging” erreicht man die Konsole, in der Log-Informationen über sämtliche Kommandos an den Simulator sowie dessen Rückmeldungen protokolliert werden (siehe {numref}`fig-logging`). Hier können über das Kontextmenü sowohl Einstellungen zum Logging-Verhalten vorgenommen als auch der Log-Inhalt in eine Datei geschrieben werden.

Außerdem bietet diese Konsole die Möglichkeit, den Simulator direkt mit Kommandos in der Kommandozeile zu steuern. Eine Liste der verfügbaren Kommandos lässt sich mit dem Kommando help aufrufen.

```{figure} ../figures/logging.png
:alt: Header
:width: 400
:figclass: center-figure
:name: fig-logging

: PersoSim mit Logging-Daten
```


### Smartphone als Kartenleser
Die BSI TR-03112-6 sieht die Funktion ”Remote-IFD” vor, auch bekannt unter dem Namen ”Smartphone als Kartenleser”. Mit dieser Funktion lässt sich ein NFC-fähiges Smartphone als Kartenleser im Kontext des Personalausweises nutzen. Auch PersoSim unterstützt diese Funktion sowohl in der Desktop-Anwendung als auch in der Android-App und kann so von einem eID-Client per Netzwerk angesprochen werden.

Um diese Funktion zu nutzen, muss zunächst die Anbindung im Menüpunkt ”Reader Type” → ”UseRemote IFD” entsprechend umgestellt werden. Der aktive Verbindungstyp wird stets im oberen Bereich der Kartenleser-Oberfläche (oberhalb des PinPads) angezeigt.

Damit ein eID-Client mit PersoSim per Remote-IFD kommunizieren kann, müssen die beiden Geräte/Programme miteinander gekoppelt werden. Der entsprechende Dialog ist im Menü ”Reader Type” → ”Configure RemoteIFD” erreichbar (siehe {numref}`fig-configurationRemoteIFD`).

Im oberen Bereich werden bereits gekoppelte Anwendungen angezeigt. Bei Bedarf können diese hier per Kontextmenü entfernt werden.

Im mittleren Bereich kann der Kopplungsvorgang durch Klick auf ”Start pairing” initiiert werden. Dies unterbricht vorhandene Verbindungen für die Dauer des Koppelvorgangs und zeigt den notwendigen Kopplungscode an. Mithilfe dieses Kopplungscodes kann sich ein entsprechender eID-Client dann mit PersoSim verbinden (siehe hierzu auch die Dokumentation des eID-Clients). Nach einer erfolgreichen Kopplung erfolgt die gegenseitige Authentisierung zertifikatsbasiert, sodass keine weitere Kopplung mehr notwendig ist.

```{figure} ../figures/configurationRemoteIFD.png
:alt: Header
:width: 350
:figclass: center-figure
:name: fig-configurationRemoteIFD

: Konfiguration Remote-IFD
```
<br>

Zu guter Letzt lässt sich im unteren Bereich der Name dieser PersoSim-Instanz konfigurieren. Dieser wird von eID-Clients zur Kopplung und zum Wiederverbinden genutzt, damit der Benutzer die entsprechende Gegenstelle auswählen kann.