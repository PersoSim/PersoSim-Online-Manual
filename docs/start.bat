@ECHO OFF
REM Batch-Datei zum Öffnen von build/html/index.html im Browser

SET FILEPATH=%CD%\build\html\index.html

IF EXIST "%FILEPATH%" (
    START "" "%FILEPATH%"
) ELSE (
    ECHO Fehler: Die Datei "%FILEPATH%" wurde nicht gefunden.
    PAUSE
)
