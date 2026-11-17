(controler)=
# PersoSim Controller

Der PersoSim Controller ist ein separates Executable und ermöglicht die Fernsteuerung von PersoSim
per Konsole auf dem lokalen System. Das Executable liegt parallel zum PersoSim Executable. Es
werden die folgenden Kommandos unterstützt:
* *start* (um PersoSim zu starten)
* *stop* (um PersoSim zu stoppen)
* *restart* (um PersoSim neu zu starten)
* *loadperso* (um ein vorgegebenes Profil in PersoSim bereitzustellen)
* *sendapdu* (um eine APDU an den Simulator zu schicken)
* *reset* (um den Simulator analog zum Smartcard-Reset zu resetten)
* *help* (um die verfügbaren Kommandos anzuzeigen)

Die Kommandos *start*, *stop* und *restart* dienen dazu, das PersoSim Executable bzw. den entsprechenden Prozess zu steuern. Die anderen Kommandos werden an den laufenden PersoSim Prozess per SOAP geschickt.
Nachfolgend ist die Ausgabe des *help* Kommandos (unter Windows: *PersoSimControllerc.exe help*)
dargestellt. Dort werden detailliert die verfügbaren Kommandos beschrieben:

```
PersoSimControllerc.exe <start|stop|restart> <fullPathToExecutable>
    --> Start, stop or restart PersoSim.
    Example (Windows): PersoSimControllerc.exe start "C:\PersoSimDir\PersoSim.exe"
    Example (Linux)  : PersoSimController stop "/home/someuser/PersoSimDir/PersoSim"
    Example (MacOS)  : cd /home/someuser/PersoSimDir/PersoSim.app/Contents/Eclipse; ../MacOS/PersoSimController restart ../MacOS/PersoSim
or:
PersoSimControllerc.exe loadperso <absolutePathToPersoFile>|<nameOfPredefinedStandardProfile>
    --> Load a personalization file into PersoSim.
        A standard profile is named by its id, its file name (with or without '.perso'),
        its personalization class or its profile number.
    Example (Absolute Path, Windows): PersoSimControllerc.exe loadperso "C:\PersoSimDir\profiledir\nPA_02_A-MUSTERMANN.perso"
    Example (Standard Profile)      : PersoSimControllerc.exe loadperso nPA_03_J-MUSTERMANN.perso
    Example (by its id)             : PersoSimControllerc.exe loadperso nPA_03
or:
PersoSimControllerc.exe sendapdu <apduAsHexString>
    --> Send an APDU in HEX String format to PersoSim.
    Example: PersoSimControllerc.exe sendapdu 0084000000
or:
PersoSimControllerc.exe reset
    --> Reset PersoSim analogous to a Smartcard Reset.
or:
PersoSimControllerc.exe help
    --> Show this usage information.

```

Ein mitgeliefertes Profil lässt sich beim Kommando *loadperso* über seine Kennung (z.B. nPA_03), seinen Dateinamen (mit oder ohne „.perso“) oder seinen kompletten absoluten Dateipfad angeben. Ein per *loadperso* geladenes Profil zeigt PersoSim in der Profilauswahl so an, als wäre es in der Oberfläche ausgewählt worden. Eine laufende Simulation wird dabei beendet, und ungespeicherte Änderungen an einem Profil werden verworfen.

Die SOAP-Schnittstelle von PersoSim kann auch direkt unabhängig vom PersoSim Controller
verwendet werden. Die zugehörige WSDL kann in einem Standard-Browser aufgerufen werden. Die
entsprechende URL lautet: [http://localhost:8890/persosim/PersoSimRemoteControl?wsdl](http://localhost:8890/persosim/PersoSimRemoteControl?wsdl)

