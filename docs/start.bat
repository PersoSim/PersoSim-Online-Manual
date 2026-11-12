@ECHO OFF
REM Batch file that opens build/html/index.html in the browser

SET FILEPATH=%CD%\build\html\index.html

IF EXIST "%FILEPATH%" (
    START "" "%FILEPATH%"
) ELSE (
    ECHO Fehler: Die Datei "%FILEPATH%" wurde nicht gefunden.
    PAUSE
)
