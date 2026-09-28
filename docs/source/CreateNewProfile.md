# PersoSim Editor Handbuch 

(profile)=
## Profile
In PersoSim nutzen wir nicht nur typische Profile, wie sie im physischen Personalausweis verwendet werden, sondern auch Unionsbürgerkarten und Smart-eID. Informationen zu den Profilen der jeweiligen Varianten stellen wir in den folgenden Dokumenten bereit:

- Klassischer Personalausweis: [PersoSim Personalisierungsdaten nPA 2024](https://persosim.github.io/manuals/nPA-PersoSim_Personalisierungsdaten_V3-2024.pdf)
- Unionsbürgerkarte: PersoSim [Personalisierungsdaten eID UB 2024](https://persosim.github.io/manuals/eID-UB-PersoSim_Personalisierungsdaten_V2-2024.pdf)

(musterkarten-npa)=
### Übersicht der Musterkarten (nPA)
Die folgende Tabelle gibt einen Überblick über die Personalisierungsdaten der mitgelieferten Musterkarten des klassischen Personalausweises (nPA). Sie entspricht dem Dokument [PersoSim Personalisierungsdaten nPA 2024](https://persosim.github.io/manuals/nPA-PersoSim_Personalisierungsdaten_V3-2024.pdf) (Version 3.0). Die Musterkarten decken sowohl gewöhnliche als auch seltenere, aber zulässige Sonderfälle ab. Musterkarte 10 demonstriert dabei die maximal zulässigen Feldlängen gemäß PAuswV Anhang 3 Nr. 10.

| Feld | Musterkarte 01 | Musterkarte 02 | Musterkarte 03 | Musterkarte 04 | Musterkarte 05 | Musterkarte 06 | Musterkarte 07 | Musterkarte 08 | Musterkarte 09 | Musterkarte 10 | Musterkarte 11 | Max. Feldlänge¹ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Besonderheiten |  | Angabe Staatsangehörigkeit leer |  | kein Vorname; unvollständiges Geburtsdatum | unvollständiges Geburtsdatum, Geburtsname fehlt, Angabe Staatsangehörigkeit fehlt | mit Ordens-/ Künstlername | wohnungslos | Wohnsitz im Ausland, mit Ordens-/ Künstlername | Alter <10 Jahre; eID-Funktion deaktiviert | lange Feldinhalte; keine Hausnummer | Gültigkeitsende erreicht |  |
| Ausgebender Staat (Ländercode) | D | D | D | D | D | D | D | D | D | D | D |  |
| Gültig von (nur informativ) | 2024-07-01 | 2024-07-01 | 2024-07-01 | 2024-07-01 | 2024-07-01 | 2024-07-01 | 2024-07-01 | 2024-07-01 | 2024-07-01 | 2024-07-01 | 2024-06-15 |  |
| Gültig bis | 2034-06-30 | 2034-06-30 | 2034-06-30 | 2034-06-30 | 2034-06-30 | 2034-06-30 | 2034-06-30 | 2034-06-30 | 2030-10-30 | 2034-06-30 | 2024-06-30 |  |
| Staatsangehörigkeit (Ländercode) | D | (absent: id-eIDDGMissing DG10) | D | D | (absent: id-eIDDGMissing DG10) | D | D | D | D | D | D |  |
| Geschlecht (nur informativ) | weiblich | männlich | weiblich | männlich | weiblich | männlich | weiblich | männlich | weiblich | männlich | weiblich |  |
| Doktorgrad |  |  | DR. |  |  | DR.EH.DR. |  | DR.HC. |  | AHIHIHIHIHIHIHIHIHIHIHIHIHIHIHIZ |  | 32 |
| Familienname | MUSTERMANN | MUSTERMANN | MUSTERMANN | ĆOSIĆ | ÖZM̂EN | VON DREBENBUSCH-DALGOẞEN | LERCH | HILLEBRANDT | SCHUSTER | ABCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCBCZ | MÜLLER | 120 |
| Geburtsname | GABLER |  | VON MÜLLER-SCHWARZENBERG |  | (absent: id-eIDDGMissing DG13) | WEIẞ | BJØRNSON |  |  | ADEDEDEDEDEDEDEDEDEDEDEDEDEDEDEDEDEDEDEDEDEDEDEDEDEDEDEDEDEDEDEDEDEDEDEDEDEDEDEZ |  | 80 |
| Vorname(n) | ERIKA | ANDRÉ | JOHANNA EDELTRAUT LISBETH | --- | AĞÇA | HANS-GÜNTHER | ANNEKATHRIN | KARL | LILLY | AFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGFGZ | HILDEGARD | 80 |
| Geburtsdatum | 1984-08-12 | 2001-06-17 | 1968-04-21 | 1994-09-XX | 1989-XX-XX | 1946-01-25 | 1976-07-05 | 1972-06-17 | 2015-03-30 | 2000-01-01 | 1959-02-04 |  |
| Datum für Altersverifikation | 1984-08-12 | 2001-06-17 | 1968-04-21 | 1994-09-30 | 1989-12-31 | 1946-01-25 | 1976-07-05 | 1972-06-17 | 2015-03-30 | 2000-01-01 | 1959-02-04 |  |
| Geburtsort | BERLIN | FRANKFURT (ODER) | MÜNCHEN | PRIŠTINA | DESSAU-ROẞLAU | BREMERHAVEN | BAD KÖNIGSHOFEN I. GRABFELD | TRIER | MÜHLHAUSEN/THÜRINGEN | ALMLMLMLMLMLMLMLMLMLMLMLMLMLMLMLMLMLMLMLMLMLMLMLMLMLMLMLMLMLMLMLMLMLMLMLMLMLMLMZ | SAARBRÜCKEN | 80 |
| Adresse – Wohnsitz im Ausland | Nein | Nein | Nein | Nein | Nein | Nein | Nein | Ja | Nein | Nein | Nein |  |
| Adresse – Wohnungslos | Nein | Nein | Nein | Nein | Nein | Nein | Ja |  | Nein | Nein | Nein |  |
| Adresse – PLZ | 51147 | 03222 | 12059 | 68159 | 01129 | 22043 | 06108 |  | 99817 | A12345678Z | 44225 | 10 |
| Adresse – Ort | KÖLN | LÜBBENAU/SPREEWALD | BERLIN | MANNHEIM | DRESDEN | HAMBURG | HALLE (SAALE) |  | EISENACH | ANONONONONONONONONONONONONONONONONONONOZ | DORTMUND | 40 |
| Adresse – Straße | HEIDESTRAẞE 17 | EHM-WELK-STRAẞE 33 | BOUCHÉSTR. 68 A | F4 14-15 | GROẞENHAINER STR. 133/135 | WEG NR. 12 8E |  |  | MARIENSTRAẞE 144 | APQPQPQPQPQPQPQPQPQPQPQPQPQPQPQPQPQPQPQPQPQPQPQPQZ | HARKORTSTR. 58 | 50 |
| Adresse – Wohnort-ID | 02760503150000 | 02761200660196 | 02761100000000 | 02760802220000 | 02761406120000 | 02760200000000 | 02761500020000 |  | 02761600560000 | 02761100000000 | 02760509130000 | 14 |
| Ordens-/ Künstlername |  |  | ORDENSSCHWESTER JOHANNA |  |  | FREIHERR ZU MÖCKERN-WINDENSBERG |  | GRAF V. LÝSKY |  | AJKJKJKJKJKJKJKJKJKJKJKJKJKJKJKZ |  | 32 |

¹ Aktuell genutzte maximale Feldlänge gemäß PAuswV Anhang 3 Nr. 10.


(musterkarten-ub)=
### Übersicht der Musterkarten (Unionsbürgerkarte)
Die folgende Tabelle gibt einen Überblick über die Personalisierungsdaten der mitgelieferten Musterkarten der eID-Karte für Unionsbürger (UB). Sie entspricht dem Dokument [Personalisierungsdaten eID UB 2024](https://persosim.github.io/manuals/eID-UB-PersoSim_Personalisierungsdaten_V2-2024.pdf) (Version 2.0). Die Musterkarten decken u. a. einen Wohnsitz im Ausland, mehrere Vor- und Nachnamen sowie diakritische und skandinavische Sonderzeichen ab.

| Feld | Musterkarte UB01 | Musterkarte UB02 | Musterkarte UB03 | Musterkarte UB04 | Musterkarte UB05 |
|---|---|---|---|---|---|
| Besonderheiten |  | Wohnort im Ausland, Mehrere Vornamen, Diakritische Zeichen | Mehrere Vor- und Nachnamen, Diakritische Zeichen | Unvollständiges Geburtsdatum, Adresse aus Quadratestadt | Wohnort im Ausland, Skandinavische Sonderzeichen |
| Ausgebender Staat (Ländercode) | D | D | D | D | D |
| Gültig von (nur informativ) | 2024-07-01 | 2024-07-01 | 2024-07-01 | 2024-07-01 | 2024-07-01 |
| Gültig bis | 2034-06-30 | 2034-06-30 | 2034-06-30 | 2034-06-30 | 2034-06-30 |
| Staatsangehörigkeit (Ländercode) | FIN | CZE | ESP | IRL | DNK |
| Geschlecht (nur informativ) | weiblich | männlich | weiblich | männlich | weiblich |
| Doktorgrad |  |  | DR. | DR.HC. |  |
| Familienname | MUSTERMANN | MARTINÍK | GARCIA LÓPEZ | Ó RUDAÍ | LÆRKE |
| Geburtsname | MEIKÄLÄINEN | VOMÁČKA |  |  | BJØRNSON |
| Vorname(n) | MAIJA | TOMÁŠ KAREL | MARIA ELENA INÊS | PADDY | ÅSA |
| Geburtsdatum | 1988-04-21 | 1961-08-17 | 1964-08-12 | 1953-09-XX | 1995-06-12 |
| Datum für Altersverifikation | 1988-04-21 | 1961-08-17 | 1964-08-12 | 1953-09-30 | 1995-06-12 |
| Geburtsort | KANKAANPÄÄ | MÜNCHEN | GRANADA | BALLYCLOUGH | OSLO |
| Adresse – Country | D | GBR | D | D | FIN |
| Adresse – State |  |  |  |  |  |
| Adresse – PLZ | 51147 | W1H 8BR | 99817 | 68161 | 81100 |
| Adresse – Ort | KÖLN | LONDON | EISENACH | MANNHEIM | KONTIOLAHTI |
| Adresse – Straße | HEIDESTRAẞE 17 | 56 CROWN STREET | AMTSPLATZ 4A | R3 3-5 | AHLSTRÖMINKATU 2 |
| Adresse – Wohnort-ID | 02760503150000 | 08260000000000 | 02761600560000 | 02760802220000 | 02460000000000 |
| Ordens-/ Künstlername |  |  | SCHWESTER ANNA | MISTER BARISTA |  |


(chap:CreateNewProfil)= 
### Erstellen eines eigenen Profiles 
Zusätzlich zu den mitgelieferten Profilen innerhalb von PersoSim besteht die Möglichkeit, eigene Profile zu erstellen. Profile bestehen aus einem XML-File, das alle relevanten Informationen für die Simulation enthält. Damit der Anwender aber nicht im XML-File editieren muss, gibt es ein zusätzliches Werkzeug zum einfachen Editieren der Profile (siehe {numref}`fig-editor-masterfile`) Der Editor steht genauso wie der Simulator auf der Website zum Download bereit.
Die Oberfläche unterteilt sich in zwei Ansichten "Masterfile" und "eID". In der "Masterfile"-Ansicht werden die verfügbaren Passwörter sowie Schlüsselpaardaten für die sichere Verschlüsselung und Kommunikation angezeigt.


```{figure} ../figures/editor-masterfile.png
:alt: Header
:width: 500
:figclass: center-figure
:name: fig-editor-masterfile

: PersoSim Editor - Oberfläche des Masterfile
```
<br>

In der Ansicht der "eID" werden alle verfügbaren Informationen auf der Chipkarte angezeigt. Der Editor unterstützt den Anwender bei der Eingabe neuer Profile, indem er auf fehlerhafte Eingaben aufmerksam macht (siehe {numref}`fig-invalid-input`). So weist der Editor beispielsweise darauf hin, sobald der Anwender ein falsches Format des Gültigkeitsdatums oder Ländercodes eingibt. Als Basis für eigene Profile kann der Anwender natürlich auch die mitgelieferten Profile nutzen.

```{figure} ../figures/invalid-input.png
:alt: Header
:width: 500
:figclass: center-figure
:name: fig-invalid-input

: PersoSim Editor - Falsche Eingabe
```
<br>


Unter den Signatur-Einstellungen kann der Anwender ein DS-Zertifikat inkl. DS-Schlüssel eintragen, um das neue Profil auch final zu signieren (siehe {numref}`fig-signature-settings`). Die dazu notwendigen Dateien EF.CardSecurity und EF.ChipSecurity werden dabei neu erstellt, um das Profil zu vervollständigen. Erstellt man ein Profil ’from the scratch’ kann man auch ein dazugehöriges EF.CardAccess erstellen lassen. Diese personalausweisspezifischen Dateien enthalten die Standardparameter für Kryptografie und Protokolle, die durch die BSI TR-03110 und BSI TR-03127 für den deutschen Personalausweis vorgegeben werden. EF.CardAccess, EF.CardSecurity und EF.ChipSecurity lassen sich nicht mit dem Editor neu generieren und nicht manuell bearbeiten.

```{figure} ../figures/signature-settings.png
:alt: Header
:width: 300
:figclass: center-figure
:name: fig-signature-settings

: Signatur-Einstellungsfenster
```
<br>


### Öffnen eines Profiles 
Der Editor bietet außerdem die Möglichkeit, ein bereits vorhandenes, selbsterstelltes Profil zu laden. Dazu wählen Sie im Reiter „File“ den Punkt „Open“ und öffnen die gewünschte Datei (siehe {numref}`fig-open-new-profil`). 
```{figure} ../figures/load-profil.png
:alt: Header
:width: 500
:figclass: center-figure
:name: fig-open-new-profil

: Neues Profil laden
```
<br>

Das geladene Profil erscheint anschließend im Reiter „Profiles“ und kann dort wie die mitgelieferten Profile ausgewählt werden (siehe {numref}`fig-select-profil`). 

```{figure} ../figures/select-profil.png
:alt: Header
:width: 500
:figclass: center-figure
:name: fig-select-profil

: Profil auswählen
```