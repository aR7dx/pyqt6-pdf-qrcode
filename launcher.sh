#!/bin/bash

echo "===============Initialisation================="
echo "Initialisation du programme."
echo "=================Chargement==================="
echo "Chargement du programme en cours..."
echo

# Chemin vers le dossier des fichiers temporaires
TEMP_FOLDER="./temp"

# Vérification de l'existence du dossier temporaire
if [ ! -d "$TEMP_FOLDER" ]; then
	mkdir "$TEMP_FOLDER"
fi

# Chemin vers le fichier temporaire de sortie
TEMP_OUTPUT_FILE="$TEMP_FOLDER/temp_output.txt"

# Suppression du fichier temporaire de sortie s'il existe
if [ -f "$TEMP_OUTPUT_FILE" ]; then
	rm "$TEMP_OUTPUT_FILE"
fi

# Chemin vers le fichier Python
PYTHON_SCRIPT="./sources/main.py"

# Exécution du script Python et capture de la sortie
python3 "$PYTHON_SCRIPT" 2> "$TEMP_OUTPUT_FILE"
PYTHON_RESULT=$?


# Vérification du code de retour du script Python
if [ $PYTHON_RESULT -eq 0 ]; then
    echo "+======================================================+"
    echo
else
    # Affichage du message d'échec
    echo "+=======================Erreur============================+"
    echo "^| Le chargement du programme a échoué. Essayez à nouveau. ^|"
    echo "+=========================================================+"
    echo
    echo "+========================================Erreur==========================================+"
    echo "^| Consulter le fichier 'temp_output' situé dans le dossier 'temp' à la racine du projet. ^|"
    echo "+========================================================================================+"
fi


read -p "Appuyez pour arrêter le programme..."