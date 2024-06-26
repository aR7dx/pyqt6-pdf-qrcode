@echo off
chcp 65001 > nul

title Launcher (pyqt6-pdf-qrcode)
color D

:create_log
setlocal enabledelayedexpansion
for /f "tokens=1-6 delims=/:. " %%a in ("%date% %time%") do (
    set "DD=%%a"
    set "MM=%%b"
    set "YYYY=%%c"
    set "HH=%%d"
    set "Min=%%e"
    set "Sec=%%f"
)
set "Sec=!Sec:~0,2!"
set "TEMP_LOG_FILE=LOG_%DD%%MM%%YYYY%_%HH%%Min%%Sec%.log"
goto jump

:start
call :create_log

:jump
echo ===============Initialisation=================
echo Initialisation du programme.
echo =================Chargement===================
echo Chargement du programme en cours...

rem Chemin vers le dossier temporaire permanent
set TEMP_FOLDER=".\temp"

rem Vérification de l'existence du dossier temporaire
if not exist "%TEMP_FOLDER%" mkdir "%TEMP_FOLDER%"

rem Chemin vers le fichier Python
set PYTHON_SCRIPT=".\sources\main.py"

rem Exécution du script Python et capture de la sortie
python "%PYTHON_SCRIPT%" 2>> "%TEMP_FOLDER%\%TEMP_LOG_FILE%"
set PYTHON_RESULT=%errorlevel%


rem Vérification du code de retour du script Python
if %PYTHON_RESULT% equ 0 (
    echo.
) else (
    rem Affichage du message d'échec
    echo +========================================Erreur====================================================+
    echo ^| Consulter le fichier %TEMP_LOG_FILE% situé dans le dossier %TEMP_FOLDER% à la racine du projet. ^|
    echo +==================================================================================================+
    timeout /t 3
    echo.
    goto start

)

pause
