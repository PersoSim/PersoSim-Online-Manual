# Neuigkeiten
Die folgenden Neuigkeiten sind chronologisch sortiert und die neuesten Einträge stehen oben.

## Android Smart Card Emulator Version 4.0 
```{hint}
Die mit PersoSim kompatible Version 4.0 der App [„Smart Card Emulator“](https://github.com/frankmorgner/vsmartcard) ist jetzt direkt über den [F-Droid Store](https://f-droid.org/de/packages/com.vsmartcard.acardemulator) verfügbar. Damit ist eine manuelle Installation nicht mehr länger notwendig. Mithilfe der App kann ein Android Smartphone über seine NFC-Schnittstelle in Verbindung mit der PersoSim-Schnittstelle VSmartCard eine eID-Karte simulieren. Wir möchten uns für diese Veröffentlichung bei Frank Morgner, dem Entwickler des Projekts VSmartCard, bedanken.
```


## PersoSim 1.8 mit neuer Oberfläche und integriertem Editor
```{hint}
Mit Version 1.8 erhält PersoSim eine neu gestaltete Oberfläche, die in drei Schritten durch die Simulation führt: Profilauswahl, Technologieauswahl und Simulation. Die wichtigsten Änderungen:

- Integrierter Editor: Der bisher separate PersoSim Editor ist in PersoSim aufgegangen. Profile lassen sich direkt in der Profilauswahl bearbeiten, prüfen und speichern. RI-Schlüssel, Signatur-Einstellungen, Trust Points und der JSON-Export stehen im Expertenmodus zur Verfügung.
- Neue Profile: Profile für den elektronischen Aufenthaltstitel (eAT) mit den Datengruppen DG19 und DG20, zwei Profile mit dem vollständigen zulässigen Zeichensatz sowie Sonderprofile für Protokoll- und Datengruppen-Sonderfälle.
- Prüfung der Technologie: Für jede Technologie prüft PersoSim vor dem Start, ob die Voraussetzungen erfüllt sind, und zeigt das Ergebnis direkt an.
- Passworteingabe: Beim Standardleser werden PIN, CAN und PUK direkt in PersoSim eingegeben, auf Wunsch auch automatisch.
- Helles und dunkles Farbschema nach der Einstellung des Betriebssystems.

Die Beschreibung der neuen Oberfläche findet sich im Kapitel [PersoSim Simulator](Using.md).
```
<hr style="height: 2px; background: #00509B;">


## PersoSim 1.6 veröffentlicht mit Anbindung an Comprion CL Verify
```{hint}
In diesem Release wurde als Hardware zur Kommunikation zwischen Simulator und Kartenleser der [Comprion CL Verify](https://www.comprion.com/products-solutions/products-solutions-a-z/cl-verify-a/) integriert. Dieses Gerät übernimmt die Kommunikation auf den unteren Layern und übersetzt die empfangenen Signale in eine APDU, die an PersoSim weitergeleitet wird. Dieser bearbeitet die APDU und schickt das Ergebnis zurück an den CL Verify, welcher es als R-APDU zurück an den Kartenleser gibt.

Organisationen und Firmen, die bereits im Besitz eines CL Verify sind, können diesen mit Release 1.6 nun auch in Kombination mit PersoSim einsetzen.

```
<hr style="height: 2px; background: #00509B;">


## Experimentelle Version veröffentlicht für Chameleon Mini
```{hint}
Zur Integration eines Chameleon Mini gibt es nun eine experimentelle Version 1.5.5 von PersoSim. Da die benötigten Protokolle, was Feldstärke, Timing usw. angeht, zu anspruchsvoll für den Chameleon Mini sind, steht diese Version nicht als offizielles Release zur Verfügung. Stattdessen kann sie zu Testzwecken und als Basis für weitere Entwicklungen genutzt werden. Detailliertere Infos zur Nutzung gibt es hier: [PersoSim und Chameleon Mini](https://persosim.github.io/chameleon_mini.html).
```
<hr style="height: 2px; background: #00509B;">



## PersoSim Version 1.4 veröffentlicht mit Remote-Schnittstelle und verbessertem Logging
```{hint}
Die neue Version 1.4 des Personalausweis-Simulators liefert die folgenden Features:

- Terminal-Schnittstelle: Zur einfacheren Ansteuerung von PersoSim ist nun eine Remote-Schnittstelle integriert, über die sich PersoSim fernsteuern lässt. Diese Schnittstelle soll den Einsatz für Continuous Integration (CI) erleichtern. Die unterstützten Kommandos werden im aktualisierten Anwenderhandbuch beschrieben.
- Remote-IFD-Schnittstelle: Der Kopplungscode kann weiterhin zufällig generiert bzw. frei gewählt werden. Allerdings ist der Kopplungscode von nun an beim Start auf ‚1234‘ eingestellt, was die Kopplung im Testkontext vereinfachen soll.
- Logging: Das Logging in PersoSim wurde grundlegend überarbeitet, sodass der Anwender nun viele Möglichkeiten hat, das Logging für seine Bedürfnisse anzupassen. Nähere Infos dazu finden sich ebenfalls im aktualisierten Anwenderhandbuch.

Wer sich wundert, wo die Version 1.3 geblieben ist: Die Versionsnummerierung wurde umgestellt, sodass gerade Versionsnummern (minor) nun immer die aktuellen Releases kenntlich machen. Ungerade Nummern stehen für Zwischenversionen, die bei Bedarf für Testzwecke bereitgestellt werden.

```
<hr style="height: 2px; background: #00509B;">


## PersoSim Version 1.2 veröffentlicht
```{hint}
Die Version 1.2 des Personalausweis-Simulators bringt gleich mehrere neue Funktionen:

- Android: Neue Anbindung des Android Smart Card Emulators aus dem vsmartcard-Projekt an PersoSim. Der Android Smart Card Emulator kann genutzt werden, um PersoSim mithilfe eines Android-Geräts mit NFC und eines RFID-Kartenlesers anzusprechen. Der Emulator kann über F-Droid auf dem Android-Smartphone installiert werden, siehe [https://f-droid.org/de/packages/com.vsmartcard.acardemulator/](https://f-droid.org/de/packages/com.vsmartcard.acardemulator/). Beide Geräte (PersoSim und Android) müssen sich per Netzwerk erreichen können und die korrekte IP-Adresse und der Port müssen im Android Smart Card Emulator eingetragen werden. PersoSim stellt QR-Codes zur Verfügung, die in den Einstellungen der App gescannt werden können, um die entsprechenden Werte zu setzen.
- Simulator: Zusätzliche Unterstützung des Protokolls CAv3. Mit dem Protokoll Chip Authentication in Version 3 (CAv3) sind die Protokolle in PersoSim nun vollständig. CAv3 ist eine Alternative zu CAv2 und Restricted Identification (RI) und bietet neben der starken expliziten Authentifizierung des Ausweises und der bereitgestellten sektorspezifischen Kennungen gegenüber dem Terminal u. a. auch die Sicherstellung der Pseudonymität des Ausweises ohne die Notwendigkeit, dieselben Schlüssel auf mehreren Chips zu verwenden. Hinweis: Im Zusammenhang mit der Umsetzung von CAv3 wurde die Profilstruktur erweitert. Aus diesem Grund benötigt der aktuelle Simulator auch Profile, die mit dem aktuellen Editor erstellt werden. Es ist keine Abwärtskompatibilität gewährleistet. Die mitgelieferten Profile sind davon selbstverständlich nicht betroffen.
- Simulator: Unterstützung des COMPARE-Kommandos. Mit diesem Kommando lassen sich Daten auf unterschiedliche Weise vergleichen. Das Kommando ist so implementiert, dass der Mechanismus wie beim Personalausweis die Verifikation der Datengruppen DG3 (Geburtsdatum), DG8 (Ablaufdatum) und DG18 (CommunityID) unterstützt.
- Simulator: Unterstützung des ENVELOPE-Kommandos. Dieser Mechanismus kann als eine Alternative für Devices genutzt werden, die kein Extended Length unterstützen. Die einzelnen Kommandos zwischen Simulator und Terminal (und umgekehrt) werden dazu in kleinere Pakete verpackt und übertragen. Darüber hinaus wurden die Profile aktualisiert und neu signiert. Profile für die Smart-eID wurden aus dem Simulator entfernt, da sie nicht mehr benötigt werden.

Ausblick: Auch die nächste PersoSim-Version wird wieder neue Features beinhalten. Die zukünftige Version 1.4 bringt ein überarbeitetes Logging, eine Schnittstelle zur Fernsteuerung des Simulators und eine Vereinfachung beim Remote-IFD-Interface.
```
<hr style="height: 2px; background: #00509B;">


## Windows-Treiber jetzt signiert
```{hint}
Ab sofort steht endlich auch ein signierter Windows-Treiber zur Verfügung. Das Installationspaket liegt hier: [PersoSim_Win_Driver_x64.zip](https://persosim.github.io/software/PersoSim_Win_Driver_x64.zip).
Für die Installation des Windows-Treibers sind weiterhin Admin-Rechte notwendig. Dank gilt an dieser Stelle der Firma adesso, die den Treiber im Rahmen des Fidelio-Projekts signiert hat.

Ältere News befinden sich im [Archiv](https://persosim.github.io/news_archive.html).
```


## PersoSim Version 1.1 veröffentlicht
```{hint}
Zum Ende des Jahres ist nun die Version 1.1 von PersoSim erschienen. In diesem Release gibt es zwei Änderungen:
- Der Editor ermöglicht es nun dem Anwender, die RI-Schlüssel selbst zu ändern oder neu generieren zu lassen. Darüber hinaus werden jetzt beim ersten Start von PersoSim die RI-Schlüssel für jedes Profil neu ausgewürfelt. Dies dient dazu, Konflikte bei der Anmeldung auf Websites zu vermeiden.
- Im Editor lassen sich nun Profile im JSON-Format exportieren, sodass die Profile zukünftig im Emulator der AusweisApp verwendet werden können. Informationen zum JSON-Format gibt es hier: [File system](https://www.ausweisapp.bund.de/sdk/simulator.html#filesystem).
```


## PersoSim für macOS veröffentlicht
```{hint}
Endlich steht auch wieder eine Version für macOS zur Verfügung. In diesem Zusammenhang wurde das Pairing für Remote-IFD bzw. SaK einheitlich für alle drei Plattformen auf Zertifikats-Fingerprints umgestellt. Zusätzlich wurden die Sourcen für den virtuellen Kartenleser an das aktuelle macOS angepasst. Die Links zum Download der Version 1.0.1 finden sich im Kapitel [Installation](Installation.md) oder hier [Release 1.0.1](https://github.com/PersoSim/PersoSim/releases/tag/1.0.1).
```


## PersoSim Version 1.0.0 veröffentlicht
```{hint}
Version 1.0.0 des PersoSim-Simulators und des -Editors ist veröffentlicht. Zum Download stehen Versionen für Windows und Linux zur Verfügung. Die macOS-Version folgt demnächst. Die maßgeblichen Änderungen betreffen den Unterbau, sodass sich neue Änderungen zukünftig einfacher implementieren lassen. Dabei geht es um die folgenden Änderungen:
- PersoSim und der dazugehörige Editor basieren nun auf Java 17 bzw. 21 sowie auf Eclipse 2024/3
- Der Editor signiert nun die Personalisierungsdaten mit ECDSA-256, ECDSA-384 oder ECDSA-512
- Die Profile (nPA und UB) wurden aktualisiert und neu signiert
- Im Logging des Simulators werden nun auch Systeminformationen protokolliert
```


## PersoSim-Präsentation im Rahmen der DIF AG eID
```{hint}
Im Rahmen der 19. Sitzung der DIF AG eID beim BSI in Bonn wurde PersoSim präsentiert. Dabei wurden der aktuelle Stand des Projekts dargestellt und eine Demo zu PersoSim gegeben. Die Demo hat sich dabei von der Installation des Treibers für den virtuellen Kartenleser über die Nutzung des Simulators bis zur Kommunikation zwischen zwei HCE-Smartphones erstreckt. Anschließend wurden mit den Teilnehmern ihre Einsatzzwecke von PersoSim sowie ihre Erweiterungswünsche und Verbesserungsvorschläge diskutiert. Die Folien zum Vortrag finden sich hier: [DIF-AG-eID_PersoSim-Workshop_20240307.pdf](https://persosim.github.io/docs/DIF-AG-eID_PersoSim-Workshop_20240307.pdf).
```


## Weiterentwicklung von PersoSim gestartet
```{hint}
Aktuell werden neue Anforderungen für die Weiterentwicklung von PersoSim gesammelt. Dazu finden Gespräche mit unterschiedlichen Stakeholdern statt; die Anforderungen werden gesammelt, bewertet und eingeordnet, um sie dann zu implementieren. Es wird also zukünftig wieder neue Releases geben. Neuigkeiten gibt es auch über den neuen Mastodon-Account: [mastodon.social/@persosim](https://mastodon.social/@persosim).
```


## PersoSim 0.18.3 veröffentlicht
```{hint}
Der Simulator für den deutschen Personalausweis steht nun in Version 0.18.3 zur Verfügung. Die Änderungen erstrecken sich auf die Smart-eID, sodass der Simulator nun neue Profile für die Smart-eID beinhaltet, die zusätzlich mit dem Editor bearbeitet werden können.
```


## PersoSim jetzt auch auf der BSI-Website
```{hint}
Das BSI hat auf seiner Website nun eine eigene [Seite](https://www.bsi.bund.de/PersoSim) für PersoSim angelegt. Dort gibt es alle Informationen zum Simulator und den dazugehörigen Tools in kompakter Form. Als Teil der eID-Infrastruktur ist PersoSim ein wichtiger Mosaikstein, um die Interoperabilität der Komponenten im deutschen eID-System sicherzustellen. Die Testinfrastruktur setzt sich zu diesem Zweck aus den einzelnen Komponenten der eID-Infrastruktur zusammen, um den Herstellern der einzelnen Komponenten Testmöglichkeiten sowie Testwerkzeuge an die Hand zu geben. Für darüber hinausgehende Tests – wie bspw. die Integration des Simulators in die bestehende Continuous Integration – stehen die Entwickler und Berater der secunet gerne zur Verfügung.
```


## PersoSim 0.17.2 veröffentlicht
```{hint}
Der Ausweis-Simulator PersoSim steht nun in Version 0.17.2 mit den folgenden Änderungen bereit:
- Remote-IFD-Schnittstelle: Aktualisierung auf v2 gemäß Ergänzung [TR-03112-6](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03112/TR-03112_node.html) und Fehlerbehebungen bei der Verbindung mit der AusweisApp
- Aktualisierung der Handbücher: Die Handbücher wurden überarbeitet und stehen zudem nun auch in englischer Sprache bereit
- Einstellung von x86: PersoSim steht zukünftig nicht mehr für x86-Systeme bereit
- Kleinere Fehlerbehebungen im Simulator z. B. beim Laden von Profildateien unter Android oder der Kartenkommunikation in bestimmten Situationen
```


## secuview berichtet über PersoSim
```{hint}
In der Ausgabe 2/2017 der secuview gibt es einen Artikel zu PersoSim. Holger Funke beschreibt dort den Simulator und die Einsatzmöglichkeiten. Der Artikel steht im Kapitel [Publikationen](Publication.md) zur Verfügung oder direkt über diesen [Link](https://persosim.github.io/docs/sec_PersoSim_secuview_2_2017_offprint_DE.pdf).
```