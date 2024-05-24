@echo off
setlocal

title Launcher Scanner Qrcode Application
color D

echo ===============Initialisation=================
echo Initialisation du programme.
echo =================Chargement===================
echo Chargement du programme en cours...
echo.

rem Chemin vers le dossier temporaire permanent
set TEMP_FOLDER=".\temp"

rem Vérification de l'existence du dossier temporaire
if not exist "%TEMP_FOLDER%" mkdir "%TEMP_FOLDER%"

rem Suppression du fichier temporaire de sortie s'il existe
if exist "%TEMP_OUTPUT_FILE%" del "%TEMP_OUTPUT_FILE%"

rem Chemin vers le fichier temporaire de sortie
set TEMP_OUTPUT_FILE=%TEMP_FOLDER%\temp_output.txt

rem Chemin vers le fichier Python
set PYTHON_SCRIPT=".\sources\main.py"

rem Exécution du script Python et capture de la sortie
python "%PYTHON_SCRIPT%" 2> "%TEMP_OUTPUT_FILE%"
set PYTHON_RESULT=%errorlevel%


rem Vérification du code de retour du script Python
if %PYTHON_RESULT% equ 0 (
    echo +======================================================+
    echo.
) else (
    rem Affichage du message d'échec
    echo +=======================Erreur============================+
    echo ^| Le chargement du programme a échoué. Essayez à nouveau. ^|
    echo +=========================================================+
    echo.
    echo +========================================Erreur==========================================+
    echo ^| Consulter le fichier 'temp_output' situé dans le dossier 'temp' à la racine du projet. ^|
    echo +========================================================================================+

)

rem Si vous souhaitez visualiser le démarrage de l'application retirer le mot rem qui précede l'instruction pause
pause
endlocal
