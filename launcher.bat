@echo off
chcp 65001 > nul

rem defini le titre de la fenetre
title Launcher (pyqt6-pdf-qrcode)
rem met le texte du terminal en violet
color D

set ID_SESSION=0
rem Chemin vers le dossier temporaire des logs
set LOGS_FOLDER=".\logs"
rem Chemin vers le fichier Python à executer
set PYTHON_SCRIPT=".\src\main.py"

set PYTHONPATH=%PYTHONPATH%;%cd%\src

:start

if %ID_SESSION% equ 0 (
    rd /s /q "%LOGS_FOLDER%"
)

rem Vérification de l'existence du dossier temporaire
if not exist "%LOGS_FOLDER%" mkdir "%LOGS_FOLDER%"

rem Obtention de la date et de l'heure actuelles
for /f "tokens=1-6 delims=/:. " %%a in ("%date% %time%") do (
    set "DD=%%a"
    set "MM=%%b"
    set "YYYY=%%c"
    set "HH=%%d"
    set "Min=%%e"
    set "Sec=%%f"
)
rem Extraction des secondes (on ignore les centièmes)
set "Sec=%Sec:~0,2%"
rem Génération du nom de fichier de log basé sur le timestamp
set "LOG_FILE=LOG_%DD%%MM%%YYYY%_%HH%%Min%%Sec%.log"

echo ===============Initialisation=================
echo Initialisation du programme.
echo =================Chargement===================
echo Chargement du programme en cours...

rem Exécution du script Python et capture de la sortie
python "%PYTHON_SCRIPT%" 2>> "%LOGS_FOLDER%\%LOG_FILE%"
set PYTHON_RESULT=%errorlevel%

rem Vérification du code de retour du script Python
if not %PYTHON_RESULT% equ 0 (
    rem Affichage du message d'échec
    echo +========================================Erreur====================================================+
    echo ^| Consulter le fichier %LOG_FILE% situé dans le dossier %LOGS_FOLDER% à la racine du projet. ^|
    echo +==================================================================================================+
    echo.
    timeout /t 3
    set /a ID_SESSION=%ID_SESSION%+1
    goto start
)

pause
