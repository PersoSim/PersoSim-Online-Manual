@ECHO OFF
chcp 65001 >nul
pushd %~dp0
setlocal enabledelayedexpansion

if "%SPHINXBUILD%" == "" (
    set SPHINXBUILD=sphinx-build
)

REM Path of venv
set venv_dir=%cd%\..\.venv

REM Check, if the folder .venv exists
if exist "!venv_dir!\Scripts\activate.bat" (
    echo Finde bestehende virtuelle Umgebung .venv.
    call "!venv_dir!\Scripts\activate.bat"
    echo Virtuelle Umgebung aktiviert.
) else (
    echo Keine virtuelle Umgebung .venv gefunden.
    set /p use_venv="Möchtest du eine virtuelle Umgebung aktivieren? (j/n): "
    if /i "!use_venv!"=="j" (
        set /p venv_base_path="Bitte gib den Pfad zum Verzeichnis ein (z.B. ../backend): "
        set /p venv_name="Bitte gib den Namen der virtuellen Umgebung ein (z.B. .venv): "
        set venv_activate_path=!venv_base_path!\!venv_name!\Scripts\activate.bat
        if exist "!venv_activate_path!" (
            call "!venv_activate_path!"
            echo Virtuelle Umgebung aktiviert.
        ) else (
            echo Der Pfad "!venv_activate_path!" existiert nicht!
            pause
            goto end
        )
    ) else (
        echo Vorgang abgebrochen!
        pause
        goto end
    )
)

REM HTML-Build
echo Starte Build...
%SPHINXBUILD% -b html source build/html
if errorlevel 1 (
    echo.
    echo Fehlgeschlagen: 'sphinx-build' konnte die Dokumentation nicht bauen.
    echo Stelle sicher, dass Sphinx installiert ist und die Abhängigkeiten installiert sind!
    echo.
    pause
    goto end
) else (
    echo Build erfolgreich.
    REM Build run again
    echo Starte Build erneut...
    %SPHINXBUILD% -b html source build/html
    if errorlevel 1 (
        echo Fehler beim zweiten Build!
        pause
        goto end
    )
    echo HTML-Build erfolgreich.
)

REM LaTeX-Build
echo Starte LaTeX Build...
%SPHINXBUILD% -b latex source build/latex
if errorlevel 1 (
    echo.
    echo Fehlgeschlagen: 'sphinx-build' konnte die LaTeX-Dateien nicht erstellen.
    echo Stelle sicher, dass Sphinx und LaTeX korrekt installiert sind!
    echo.
    pause
    goto end
) else (
    echo Build erfolgreich.
    REM Build run again
    echo Starte Build erneut...
    %SPHINXBUILD% -b latex source build/latex
    if errorlevel 1 (
        echo Fehler beim zweiten Build!
        pause
        goto end
    )
    echo LaTex-Build erfolgreich.
)