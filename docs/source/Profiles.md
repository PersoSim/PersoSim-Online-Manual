# Profile und Profilbearbeitung

(profile)=
## Standardprofile
In PersoSim werden nicht nur typische Profile, wie sie im physischen Personalausweis verwendet werden, genutzt, sondern auch Profile des elektronischen Aufenthaltstitels (eAT), der eID-Karte für Unionsbürger (UB) sowie Sonderprofile für besondere Testfälle. Alle Profile nutzen als PIN die 123456 (Ausnahme: nPA_02 mit der Transport-PIN 12345), als CAN die 500540 und als PUK die 9876543210. Der Entsperrzähler der PUK steht bei allen Profilen auf 10.

Die folgenden Tabellen geben die Daten der mit PersoSim ausgelieferten Profile wieder, so wie sie im Bereich **Retrieved Data** angezeigt werden. Datumsangaben stehen im Format JJJJ-MM-TT; „XX“ markiert unbekannte Teile eines unvollständigen Geburtsdatums. „(nicht vorhanden)“ bedeutet, dass das Profil die Datengruppe nicht enthält; ein leeres Feld bedeutet, dass die Datengruppe ohne Inhalt vorhanden ist. „␣“ steht für ein Leerzeichen am Anfang oder Ende eines Werts.

(musterkarten-npa)=
### Übersicht der Musterkarten (nPA)
Die Musterkarten des klassischen Personalausweises decken sowohl gewöhnliche als auch seltenere, aber zulässige Sonderfälle ab. Musterkarte nPA_10 demonstriert dabei die maximal zulässigen Feldlängen gemäß [PAuswV Anlage 3](https://www.gesetze-im-internet.de/pauswv/anlage_3.html) Nr. 10. Die Profile nPA_12 und nPA_13 enthalten zusammen den vollständigen zulässigen Zeichensatz ([DIN 91379](https://docs.xoev.de/datentyp.schriftzeichen/%C3%BCbersicht) in der Einschränkung der [BSI TR-03123](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03123/TR-03123_node.html) Teil 3); statt Namen enthalten ihre Datengruppen die zulässigen Zeichen in aufsteigender Reihenfolge.

```{profile-table} nPA_
```


(musterkarten-eat)=
### Übersicht der Musterkarten (eAT)
Die Musterkarten des elektronischen Aufenthaltstitels enthalten zusätzlich die Datengruppen DG19 und DG20 (Nebenbestimmungen). Der Dokumenttyp (DG1) ist AR, AS oder AF.

```{profile-table} eAT_
```

(musterkarten-ub)=
### Übersicht der Musterkarten (Unionsbürgerkarte)
Die Musterkarten der eID-Karte für Unionsbürger decken u. a. einen Wohnsitz im Ausland, mehrere Vor- und Nachnamen sowie diakritische und skandinavische Sonderzeichen ab.

```{profile-table} UB_
```

(musterkarten-sp)=
### Sonderprofile
Die Sonderprofile unter **Unsupported Profiles** bilden Fälle ab, die ein Terminal erkennen und korrekt behandeln muss. Bis auf SP_01 basieren sie auf der Musterkarte nPA_01.

```{profile-table} SP_
```


(chap:profilesEdit)=
## Profile bearbeiten
Der früher separate PersoSim Editor ist seit Version 1.8 in PersoSim integriert. Eigene Profile entstehen, indem ein vorhandenes Profil, z. B. eines der mitgelieferten Profile, in der Profilauswahl bearbeitet und unter neuem Namen gespeichert wird. Profile bestehen weiterhin aus einer XML-Datei mit der Endung „.perso“, die alle relevanten Informationen für die Simulation enthält; der Anwender muss diese Datei aber nicht direkt bearbeiten.

### Daten bearbeiten
Alle Felder im Bereich **Retrieved Data** der Profilauswahl lassen sich direkt bearbeiten, eine eigene Schaltfläche zum Bearbeiten gibt es nicht. Mit der ersten Änderung wechselt der Bereich in den Bearbeitungsmodus: Die Überschrift lautet dann „Edit Retrieved Data“ und endet mit einem „\*“, ebenso tragen geänderte Felder und ihre Abschnitte das Suffix „\*“. Wird die letzte Änderung zurückgenommen, endet der Bearbeitungsmodus wieder.

Im Abschnitt **eID** stehen die Datengruppen des Profils. Einige Felder bieten zusätzliche Hilfen:

- **DG1: Document type** und **DG10: Nationality** sind Auswahllisten, die auch freie Eingaben erlauben. Bei DG10 zeigt ein Tooltip den Namen des Landes. Wird der Dokumenttyp auf einen Aufenthaltstitel (AR, AS, AF) geändert, kommen die Datengruppen DG19 und DG20 hinzu; beim Wechsel weg von einem Aufenthaltstitel fragt PersoSim vorher, da DG19 und DG20 mit ihrem Inhalt entfernt werden.
- **DG17: Address** ist in die Felder Straße, Ort, Bundesland bzw. Region, Ländercode und Postleitzahl gegliedert. Mit **Free Text Place** lässt sich die Anschrift als freier Text eingeben, **NO PLACE INFO** steht für eine fehlende Angabe.
- **DG18: Municipality ID** wird aus der Anschrift abgeleitet. Mit **Browse for Replacement** lässt sich der Inhalt aus einer Binärdatei (*.bin) übernehmen, **Save data** speichert ihn in eine Binärdatei.

Im Abschnitt **Credentials** lassen sich PIN, CAN und PUK sowie die Fehlbedienungszähler ändern. Ist **T-PIN** angehakt, handelt es sich um eine fünfstellige Transport-PIN.

### Prüfung der Eingaben
PersoSim unterstützt den Anwender bei der Eingabe, indem es auf fehlerhafte Eingaben aufmerksam macht (siehe {numref}`fig-invalid-input`). So weist PersoSim beispielsweise darauf hin, sobald der Anwender ein falsches Format des Gültigkeitsdatums oder Ländercodes eingibt. Ein fehlerhaftes Feld wird bereits während der Eingabe markiert, und darunter erscheint eine Meldung:

- **Rot (Fehler):** Der Wert ist ungültig. Beim Speichern wird der vorherige Wert beibehalten.
- **Gelb (Warnung):** Der Wert ist ungewöhnlich, wird aber wie eingegeben gespeichert.

Geprüft werden u. a. Formate (z. B. Datumsangaben, Ländercodes, nur Ziffern bei PIN, CAN und PUK), Längen sowie die zulässigen Zeichen gemäß [DIN 91379](https://docs.xoev.de/datentyp.schriftzeichen/%C3%BCbersicht). Namen müssen in Großbuchstaben eingegeben werden.

```{figure} ../figures/invalid-input.png
:alt: Fehlerhafte Eingaben
:width: 600
:figclass: center-figure
:name: fig-invalid-input

: Markierung fehlerhafter Eingaben
```

### Speichern eines Profils
Die Schaltfläche **Done** in der Kopfzeile von **Retrieved Data** schließt die Bearbeitung ab. Enthalten Felder fehlerhafte Werte, weist PersoSim vorher darauf hin (siehe {numref}`fig-invalid-data-dialog`): Gelb markierte Werte werden wie eingegeben gespeichert, rot markierte Felder behalten ihren vorherigen Wert. **Cancel** verwirft die Änderungen.

```{figure} ../figures/invalid-data-dialog.png
:alt: Hinweis auf fehlerhafte Werte
:width: 400
:figclass: center-figure
:name: fig-invalid-data-dialog

: Hinweis auf fehlerhafte Werte beim Speichern
```

Anschließend fragt PersoSim, ob die geänderten Daten in eine Datei gespeichert werden sollen, und öffnet einen Dateidialog. Als Dateiname wird der bisherige Name vorgeschlagen; vor dem Überschreiben einer Datei fragt PersoSim nach. Nach dem Speichern ist das neue Profil über **Profile from file** ausgewählt und kann direkt simuliert werden. Solange ungespeicherte Änderungen bestehen, lassen sich weder ein anderes Profil wählen noch die Simulation starten.

Ein selbst erstelltes Profil lässt sich später jederzeit über **Profile from file** wieder laden; es erscheint außerdem in der **Profile History**.

(chap:expertMode)=
### Expertenmodus
Weitere Funktionen stehen zur Verfügung, wenn in der Kopfzeile von **Retrieved Data** der **Expert Mode** angehakt ist (siehe {numref}`fig-expert-mode`). Solange ungespeicherte Änderungen bestehen, lässt sich der Expertenmodus nicht umschalten.

```{figure} ../figures/expert-mode.png
:alt: Expertenmodus
:width: 600
:figclass: center-figure
:name: fig-expert-mode

: Profilauswahl im Expertenmodus
```

**Export to JSON:** Diese Schaltfläche exportiert das Profil im JSON-Format, z. B. zur Verwendung im Simulator der AusweisApp (siehe {numref}`fig-export-json`). Informationen zum JSON-Format gibt es hier: [AusweisApp-Simulator](https://www.ausweisapp.bund.de/sdk/simulator.html#filesystem). Der Export ist nur möglich, solange keine ungespeicherten Änderungen bestehen. Profile im JSON-Format lassen sich in PersoSim nicht laden.

```{figure} ../figures/export-json.png
:alt: Export eines Profils im JSON-Format
:width: 450
:figclass: center-figure
:name: fig-export-json

: Export eines Profils im JSON-Format
```

Im Expertenmodus kommen außerdem die folgenden Abschnitte hinzu (siehe {numref}`fig-expert-mode-keys-signature`):

- **RI Key Pairs:** die Schlüsselpaare für Restricted Identification (RI), aus denen sich das Pseudonym des Profils ergibt. Über die Schaltflächen oben wird das Schlüsselpaar gewählt, darunter werden öffentlicher und privater Schlüssel angezeigt. **Generate new key material** erzeugt neue Schlüsselpaare, die mit **Done** im Profil gespeichert werden. **Persist for …** legt die Schlüsselpaare für dieses mitgelieferte Profil dauerhaft in der PersoSim-Installation ab. Beim ersten Start erzeugt PersoSim für jedes mitgelieferte Profil eigene RI-Schlüssel, um Konflikte bei der Anmeldung auf Websites zu vermeiden.
- **Signature Settings:** Hier kann der Anwender ein DS-Zertifikat (**DS Cert**, *.der) inkl. DS-Schlüssel (**DS Key**, *.pkcs8) und den Signaturalgorithmus (**DS Algo**: SHA256withECDSA, SHA384withECDSA oder SHA512withECDSA) eintragen, um das Profil zu signieren. Unter **Data Groups to be updated** wird gewählt, welche der Dateien EF.CardAccess, EF.CardSecurity und EF.ChipSecurity neu erstellt werden. Diese personalausweisspezifischen Dateien enthalten die Standardparameter für Kryptografie und Protokolle, die durch die [BSI TR-03110](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03110/TR-03110_node.html) und [BSI TR-03127](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03127/TR-03127_node.html) für den deutschen Personalausweis vorgegeben werden. **Update signed files** erstellt und signiert die gewählten Dateien neu; gespeichert wird das Profil anschließend mit **Done**. Das Speichern allein signiert ein Profil nicht neu.
- **Trust Point:** der Trust Anchor (CVCA-Zertifikat) für die Terminal Authentication. **Current trust anchor** zeigt den aktuell hinterlegten Trust Anchor. Unter **Available trust anchors** lässt sich ein anderer auswählen, **Import…** importiert ein Zertifikat aus einer Datei (*.cvcert), und **Save current…** speichert den aktuellen Trust Anchor in eine Datei. Hintergründe zu Trust Points beschreibt das Kapitel [Trust Point für Terminal Authentication](manual/TrustPoints.md).

```{figure} ../figures/expert-mode-keys-signature.png
:alt: RI-Schlüssel, Signatur-Einstellungen und Trust Point
:width: 600
:figclass: center-figure
:name: fig-expert-mode-keys-signature

: Expertenmodus mit allen Abschnitten: eID, Credentials, RI Key Pairs, Signature Settings und Trust Point
```
