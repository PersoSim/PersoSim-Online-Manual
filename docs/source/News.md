# Neuigkeiten
Die folgenden Neuigkeiten sind chronologisch sortiert und die neuesten Einträge stehen oben.

## PersoSim Version 1.4 veröffentlicht mit Remote-Schnittstelle und verbessertem Logging
```{hint}
Die neue Version 1.4 des Personalausweis-Simulators liefert die folgenden Features:

- Terminal-Schnittstelle: Zur einfacheren Ansteuerung von PersoSim haben wir nun eine Remote-Schnittstelle integriert, über die sich PersoSim fernsteuern lässt. Diese Schnittstelle soll den Einsatz für Continuous Integration (CI) erleichtern. Die unterstützten Kommandos werden im aktualisierten Anwenderhandbuch beschrieben.
- Remote-IFD-Schnittstelle: Der Kopplungscode kann weiterhin zufällig generiert werden bzw. frei gewählt werden. Allerdings ist der Kopplungscode von nun an beim Start auf ‚1234‘ eingestellt, was die Kopplung im Testkontext vereinfachen soll.
- Logging: Wir haben das Logging in PersoSim grundlegend überarbeitet, so dass der Anwender nun viele Möglichkeiten hat, das Logging für seine Bedürfnisse anzupassen. Nähere Infos dazu finden sich ebenfalls im aktualisierten Anwenderhandbuch.

Wer sich wundert, wo die Version 1.3 geblieben ist: Wir haben die Versionsnummerierung umgestellt, so dass gerade Versionsnummern (minor) nun immer die aktuellen Releases kenntlich machen. Ungerade Nummern stehen für Zwischenversionen, die wir bei Bedarf für Testzwecke bereitstellen.

```
<hr style="height: 2px; background: #00509B;">


## PersoSim Version 1.2 veröffentlicht
```{hint}
Mit der Version 1.2 des Personalausweis-Simulators stellen wir gleich mehrere neue Funktionen bereit:

- Android: Neue Anbindung des Android Smart Card Emulators aus dem vsmartcard-Projekt an PersoSim. Der Android Smart Card Emulator kann genutzt werden, um PersoSim mithilfe eines Android-Geräts mit NFC und eines RFID-Kartenlesers anzusprechen. Zur Verwendung muss derzeit noch ein aktueller Stand der App von https://github.com/frankmorgner/vsmartcard/tree/master/ACardEmulator genutzt werden. Die Version 3.5, wie sie in F-Droid zur Verfügung steht, hat derzeit noch nicht die korrekte Applet-ID, um direkt von der AusweisApp genutzt werden zu können. Beide Geräte (PersoSim und Android) müssen sich per Netzwerk erreichen können und die korrekte IP-Adresse und der Port müssen im Android Smart Card Emulator eingetragen werden. PersoSim stellt QR-Codes zur Verfügung, die in den Einstellungen der App gescannt werden können, um die entsprechenden Werte zu setzen.
- Simulator: Zusätzliche Unterstützung des Protokolls CAv3. Mit dem Protokoll Chip Authentication in Version 3 (CAv3) haben wir die Protokolle in PersoSim vervollständigt. CAv3 ist eine Alternative zu CAv2 und Restricted Identification (RI) und bietet neben der starken expliziten Authentifizierung des Ausweises und der bereitgestellten sektorspezifischen Kennungen gegenüber dem Terminal u.a. auch die Sicherstellung der Pseudonymität des Ausweises ohne die Notwendigkeit, dieselben Schlüssel auf mehreren Chips zu verwenden. Hinweis: In Zusammenhang mit der Umsetzung von CAv3 haben wir die Profilstruktur erweitert. Aus diesem Grund benötigt der aktuelle Simulator auch Profile, die mit dem aktuellen Editor erstellt werden. Es ist keine Abwärtskompatibilität gewährleistet. Die mitgelieferten Profile sind davon selbstverständlich nicht betroffen.
- Simulator: Unterstützung des COMPARE-Kommandos. Mit diesem Kommando lassen sich Daten auf unterschiedliche Weise vergleichen. Wir haben das Kommando so implementiert, dass der Mechanismus wie beim Personalausweis die Verifikation der Datengruppen DG3 (Geburtsdatum), DG8 (Ablaufdatum) und DG18 (CommunityID) unterstützt.
- Simulator: Unterstützung des ENVELOPE-Kommandos. Dieser Mechanismus kann als eine Alternative für Devices genutzt werden, die kein Extended Length unterstützen. Die einzelnen Kommandos zwischen Simulator und Terminal (und umgekehrt) werden dazu in kleinere Pakete verpackt und übertragen. Darüber hinaus haben wir die Profile aktualisiert und neu signiert. Profile für die Smart-eID haben wir im Simulator entfernt, da sie nicht mehr benötigt werden.

Ausblick: Auch die nächste PersoSim-Version wird wieder neue Features beinhalten. In der zukünftigen Version 1.4 stellen wir ein überarbeitetes Logging zur Verfügung, eine Schnittstelle zur Fernsteuerung des Simulators und eine Vereinfachung beim Remote-IFD-Interface.
```
<hr style="height: 2px; background: #00509B;">


## Windows-Treiber jetzt signiert
```{hint}
Wir freuen uns, dass wir nun endlich auch einen signierten Windows-Treiber zur Verfügung stellen können. Das Installationspaket liegt hier:  [PersoSim_Win_Driver_x64.zip](https://persosim.github.io/software/PersoSim_Win_Driver_x64.zip).
Für die Installation des Windows-Treibers sind weiterhin Admin-Rechte notwendig. Bedanken möchten wir uns an dieser Stelle bei der Firma adesso, die den Treiber im Rahmen des Fidelio-Projekts signiert hat.

Ältere News befinden sich im [Archiv](https://persosim.github.io/news_archive.html).
```


## PersoSim Version 1.1 veröffentlicht
```{hint}
Zum Ende des Jahres haben wir nun die Version 1.1 von PersoSim veröffentlicht. In diesem Release gibt es zwei Änderungen:
- Der Editor ermöglicht es nun dem Anwender, die RI-Schlüssel selbst zu ändern oder neu generieren zu lassen. Darüber hinaus werden jetzt beim ersten Start von PersoSim die RI-Schlüssel für jedes Profil neu ausgewürfelt. Dies dient dazu, Konflikte bei der Anmeldung auf Websites zu vermeiden.
- Im Editor lassen sich nun Profile im JSON-Format exportieren, so dass die Profile zukünftig im Emulator der AusweisApp verwendet werden können. Informationen zum JSON-Format gibt es hier: [File system](https://www.ausweisapp.bund.de/sdk/simulator.html#filesystem).
```


## PersoSim für macOS veröffentlicht
```{hint}
Wir freuen uns, dass wir nun auch endlich wieder eine Version für macOS zur Verfügung stellen können. In diesem Zusammenhang haben wir das Pairing für Remote-IFD bzw. SaK einheitlich für alle drei Plattformen auf Zertifikats-Fingerprints umgestellt. Zusätzlich haben wir die Sourcen für den virtuellen Kartenleser an das aktuelle macOS angepasst. Die Links zum Download der Version 1.0.1 finden sich weiter unten in Kapitel [Installation](Installation.md) oder hier [Release 1.0.1](https://github.com/PersoSim/PersoSim/releases/tag/1.0.1).
```


## PersoSim Version 1.0.0 veröffentlicht
```{hint}
Wir freuen uns, dass wir nun Version 1.0.0 des PersoSim-Simulators und des -Editors veröffentlichen können. Zum Download stehen Versionen für Windows und Linux zur Verfügung. Die macOS-Version folgt demnächst. Die maßgeblichen Änderungen haben wir im Unterbau vorgenommen, so dass wir neue Änderungen zukünftig einfacher implementieren können. Dabei geht es um die folgenden Änderungen:
- PersoSim und der dazugehörige Editor basieren nun auf Java 17 bzw. 21 sowie auf Eclipse 2024/3
- Der Editor signiert nun die Personalisierungsdaten mit ECDSA-256, ECDSA-384 oder ECDSA-512
- Die Profile (nPA und UB) wurden aktualisiert und neu signiert
- Im Logging des Simulators werden nun auch Systeminformationen protokolliert
```


## PersoSim-Präsentation im Rahmen der DIF AG eID
```{hint}
Im Rahmen der 19. Sitzung der DIF AG eID beim BSI in Bonn hatten wir die Gelegenheit, PersoSim zu präsentieren. Wir haben dort den aktuellen Stand des Projekts dargestellt und eine Demo zu PersoSim gegeben. Die Demo hat sich dabei von der Installation des Treibers für den virtuellen Kartenleser über die Nutzung des Simulators bis zur Kommunikation zwischen zwei HCE-Smartphones erstreckt. Anschließend konnten wir mit den Teilnehmern über ihre Einsatzzwecke von PersoSim und ihre Erweiterungswünsche sowie Verbesserungsvorschläge diskutieren. Die Folien zum Vortrag finden sich hier: [DIF-AG-eID_PersoSim-Workshop_20240307.pdf](https://persosim.github.io/docs/DIF-AG-eID_PersoSim-Workshop_20240307.pdf).
```


## Weiterentwicklung von PersoSim gestartet
```{hint}
Aktuell sammeln wir neue Anforderungen für die Weiterentwicklung von PersoSim. Dazu sprechen wir mit unterschiedlichen Stakeholdern, sammeln neue Anforderungen, bewerten diese und sortieren sie ein, um sie dann zu implementieren. Es wird also zukünftig wieder neue Releases geben. Neuigkeiten werden wir auch über unseren neuen Mastodon-Account bereitstellen: [mastodon.social/@persosim](https://mastodon.social/@persosim).
```


## PersoSim 0.18.3 veröffentlicht
```{hint}
Der Simulator für den deutschen Personalausweis steht nun in Version 0.18.3 zur Verfügung. Die Änderungen erstrecken sich auf die Smart-eID, so dass der Simulator nun neue Profile für die Smart-eID beinhaltet, die zusätzlich mit dem Editor bearbeitet werden können.
```


## PersoSim jetzt auch auf der BSI-Website
```{hint}
Das BSI hat auf seiner Website nun eine eigene [Seite](https://www.bsi.bund.de/PersoSim) für PersoSim angelegt. Dort gibt es alle Informationen zum Simulator und den dazugehörigen Tools in kompakter Form. Als Teil der eID-Infrastruktur ist PersoSim ein wichtiger Mosaikstein, um die Interoperabilität der Komponenten im deutschen eID-System sicherzustellen. Die Testinfrastruktur setzt sich zu diesem Zweck aus den einzelnen Komponenten der eID-Infrastruktur zusammen, um den Herstellern der einzelnen Komponenten Testmöglichkeiten sowie Testwerkzeuge an die Hand zu geben. Für darüber hinausgehende Tests – wie bspw. die Integration des Simulators in die bestehende Continuous Integration – stehen die Entwickler und Berater der secunet gerne zur Verfügung.
```


## PersoSim 0.17.2 veröffentlicht
```{hint}
Der Ausweis-Simulator PersoSim steht nun in Version 0.17.2 mit den folgenden Änderungen bereit:
- Remote-IFD-Schnittstelle: Aktualisierung auf v2 gemäß Ergänzung TR-03112-6 und Fehlerbehebungen bei der Verbindung mit der AusweisApp
- Aktualisierung der Handbücher: Die Handbücher wurden überarbeitet und stehen zudem nun auch in englischer Sprache bereit
- Einstellung von x86: PersoSim steht zukünftig nicht mehr für x86-Systeme bereit
- Kleinere Fehlerbehebungen im Simulator z.B. beim Laden von Profildateien unter Android oder der Kartenkommunikation in bestimmten Situationen
```


## secuview berichtet über PersoSim
```{hint}
In der Ausgabe 2/2017 der secuview gibt es einen Artikel zu PersoSim. Holger Funke beschreibt dort den Simulator und die Einsatzmöglichkeiten. Der Artikel steht unter ‚Veröffentlichungen‘ zur Verfügung oder direkt über diesen [Link](https://persosim.github.io/docs/sec_PersoSim_secuview_2_2017_offprint_DE.pdf).
```