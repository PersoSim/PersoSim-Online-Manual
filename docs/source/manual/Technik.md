# Technik

## Einführung
In diesem Abschnitt möchten wir technische Details veröffentlichen, die im Kontext des elektronischen Personalausweises interessant sind. Genauer gesagt geht es um die Varianten des Personalausweises, eID-Clients für den elektronischen Personalausweis sowie Open Source Projekte im Kontext des Personalausweises.


## Varianten des Personalausweises
Seit der Einführung des elektronischen Personalausweises im November 2010 wurden immer wieder Modifikationen vorgenommen. So wurde bspw. erst im Q2/2012 die Datengruppe 13 verwendet, die den möglichen Geburtsnamen des Inhabers bzw. der Inhaberin enthält oder im Q1/2013 wurde erstmals die DG10 verwendet (Staatsangehörigkeit). Diese Änderungen werden in Annex D der [BSI TR-03127](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03127/TR-03127_node.html) vollständig aufgeführt. Zusätzlich stehen diese Änderungen als DefectList gemäß [BSI TR-03129](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03129/TR-03129_node.html) zur Verfügung. 

Die sogenannte DefectList beinhaltet Produktionsfehler und -änderungen, die bei einer großen Menge von ausgegebenen Dokumenten wie dem Personalausweis unvermeidlich sind. Ein Terminal kann eine oder mehrere DefectLists über das Kommando GetDefectList anfordern. Anwendungsentwicklern im eID-Kontext wird auf dieser Basis eine Möglichkeit gegeben, die im Feld verfügbaren Varianten des Personalausweises korrekt zu behandeln und diese Varianten in ihre Software zu integrieren.

PersoSim versucht möglichst viele verschiedene Personalisierungen abzudecken, eine Übersicht über die unterschiedlichen Profile gibt es im Kapitel [Profile](#profile).


## Open Source Projekte im Kontext des Personalausweises
Im Kontext des Personalausweises gibt es unterschiedliche Projekte. Wir möchten an dieser Stelle den Open Source Projekten eine Möglichkeit bieten, sich vorzustellen. Diese Liste wird mit der Zeit erweitert. Sollten Sie Ihr Projekt in dieser Liste vermissen, kontaktieren Sie uns einfach.

- androsmex: Eine Implementierung des PACE-Protokolls für Android-Geräte mit NFC-Schnittstelle. Siehe: [code.google.com/p/androsmex](https://github.com/tsenger/androsmex)
- eIDClientCore: Eine gemeinsame Initiative der Bundesdruckerei und der Humboldt-Universität Berlin um eine clientseitige eID-Basis-Software zum Bereitstellen der eID-Funktionalität zu entwickeln. Siehe [http://sar.informatik.hu-berlin.de/BeID-lab/eIDClientCore/](http://sar.informatik.hu-berlin.de/BeID-lab/eIDClientCore/)
- openpace: Krypto-Bibliothek mit allen EAC2-Protokollen. Siehe [https://github.com/frankmorgner/openpace](https://github.com/frankmorgner/openpace)
- AusweisApp: eID-Client der Firma Governikus zum Auslesen des Personalausweises. Siehe [www.ausweisapp.bund.de](https://www.ausweisapp.bund.de/home/)
- openecard: eID-Client der Firma ecsec zum Auslesen des Personalausweises. Siehe [www.openecard.org](https://www.openecard.org/)
- vsmartcard: Projekt mit allerlei Tools rund um den Personalausweis, u.a. der SmartCardEmulator. Siehe [https://github.com/frankmorgner/vsmartcard](https://github.com/frankmorgner/vsmartcard)

