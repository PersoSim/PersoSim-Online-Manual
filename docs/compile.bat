@ECHO OFF
chcp 65001 >nul
pushd %~dp0
setlocal enabledelayedexpansion

if "%SPHINXBUILD%" == "" (
    set SPHINXBUILD=sphinx-build
)

REM Path of venv
set venv_dir=%cd%\..\.venv

REM Check whether the .venv folder exists
if exist "!venv_dir!\Scripts\activate.bat" (
    echo Found existing virtual environment .venv.
    call "!venv_dir!\Scripts\activate.bat"
    echo Virtual environment activated.
) else (
    echo No virtual environment .venv found.
    set /p use_venv="Do you want to activate a virtual environment? (y/n): "
    if /i "!use_venv!"=="y" (
        set /p venv_base_path="Enter the path to the directory (e.g. ../backend): "
        set /p venv_name="Enter the name of the virtual environment (e.g. .venv): "
        set venv_activate_path=!venv_base_path!\!venv_name!\Scripts\activate.bat
        if exist "!venv_activate_path!" (
            call "!venv_activate_path!"
            echo Virtual environment activated.
        ) else (
            echo The path "!venv_activate_path!" does not exist!
            pause
            goto end
        )
    ) else (
        echo Aborted!
        pause
        goto end
    )
)

REM HTML build
echo Starting build...
%SPHINXBUILD% -b html source build/html
if errorlevel 1 (
    echo.
    echo Failed: 'sphinx-build' could not build the documentation.
    echo Make sure that Sphinx and the dependencies are installed!
    echo.
    pause
    goto end
) else (
    echo Build successful.
    REM Run the build again
    echo Starting build again...
    %SPHINXBUILD% -b html source build/html
    if errorlevel 1 (
        echo Error in the second build!
        pause
        goto end
    )
    echo HTML build successful.
)

REM LaTeX build
echo Starting LaTeX build...
%SPHINXBUILD% -b latex source build/latex
if errorlevel 1 (
    echo.
    echo Failed: 'sphinx-build' could not create the LaTeX files.
    echo Make sure that Sphinx and LaTeX are installed correctly!
    echo.
    pause
    goto end
) else (
    echo Build successful.
    REM Run the build again
    echo Starting build again...
    %SPHINXBUILD% -b latex source build/latex
    if errorlevel 1 (
        echo Error in the second build!
        pause
        goto end
    )
    echo LaTeX build successful.
)