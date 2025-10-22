#!/bin/bash

# Chemin vers le dossier des fichiers temporaires
LOGS_FOLDER="./logs"

# Vérification de l'existence du dossier temporaire
if [ ! -d "$LOGS_FOLDER" ]; then
	mkdir "$LOGS_FOLDER"
fi

# Génération du nom de fichier log avec la date et l'heure actuelles (format : LOG_DDMMYYYY_HHMMSS.log)
LOG_FILE="$LOGS_FOLDER/LOG_$(date '+%d%m%Y_%H%M%S').log"

# Suppression du fichier temporaire de sortie s'il existe
#if [ -f "$LOG_FILE" ]; then
#	rm "$LOG_FILE"
#fi

# Chemin vers le fichier Python
PYTHON_SCRIPT="./src/main.py"

# Exécution du script Python et capture de la sortie
python3 "$PYTHON_SCRIPT" 2>> "$LOG_FILE"
PYTHON_RESULT=$?


# Vérification du code de retour du script Python
if [ $PYTHON_RESULT -eq 0 ]; then
    echo "Arrêt du programme."  
    echo 
else
    # Affichage du message d'échec
    echo "+----------------------------Erreur----------------------------+"
    echo "Le chargement du programme a échoué."
    echo 
    echo "Fichier de log : $LOG_FILE"
    echo "+--------------------------------------------------------------+"
    echo
fi


read -p "Appuyez pour arrêter le programme..."