(controler)=
# PersoSim Controller

Der PersoSim Controller ist ein separates Executable und ermöglicht die Fernsteuerung von PersoSim
per Konsole auf dem lokalen System. Das Executable liegt parallel zum PersoSim Executable. Es
werden die folgenden Kommandos unterstützt:
* Start (um PersoSim zu starten)
* Stop (um PersoSim zu stoppen)
* Restart (um PersoSim neu zu starten)
* LoadPerso (um ein vorgegebenes Profil in PersoSim bereitzustellen)
* SendApdu (um eine APDU an den Simulator zu schicken)
* Reset (um den Simulator analog zum Smartcard-Reset zu resetten)
* Help (um die verfügbaren Kommandos anzuzeigen)

Die Kommandos Start, Stop und Restart dienen dazu, das PersoSim Executable bzw. den entsprechenden Prozess zu
steuern. Die anderen Kommandos werden an den laufenden PersoSim Prozess per SOAP geschickt.
Nachfolgend ist die Ausgabe des Help Kommandos (unter Windows: PersoSimControllerc.exe help)
dargestellt. Dort werden detailliert die verfügbaren Kommandos beschrieben:

```
PersoSimControllerc.exe <start|stop|restart> <fullPathToExecutable>
--> Start, stop or restart PersoSim.
Example (Windows): PersoSimControllerc.exe start "C:\PersoSimDir\PersoSimc.exe"
Example (Linux) : PersoSimController stop "/home/someuser/PersoSimDir/PersoSim"
Example (MacOS) : cd /home/someuser/PersoSimDir/PersoSim.app/Contents/Eclipse;
../MacOS/PersoSimController restart ../MacOS/PersoSim
or:
PersoSimControllerc.exe loadperso
<absolutePathToPersoFile>|<nameOfPredefinedPersoTemplate>
--> Load a personalization file into PersoSim.
Example (Absolute Path, Windows): PersoSimControllerc.exe loadperso
"C:\\PersoSimDir\profiledir\Profile02.perso"
Example (Perso Template) : PersoSimControllerc.exe loadperso Profile03.perso
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

Die SOAP-Schnittstelle von PersoSim kann auch direkt unabhängig vom PersoSim Controller
verwendet werden. Die zugehörige WSDL kann in einem Standard-Browser aufgerufen werden. Die
entsprechende URL lautet: [http://localhost:8890/persosim/PersoSimRemoteControl?wsdl](http://localhost:8890/persosim/PersoSimRemoteControl?wsdl)

