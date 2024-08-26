# fichier principal/central du programme: son rôle est d'ordonner la création des différents composants de l'application.

import sys # importation du module sys
from PyQt6.QtWidgets import QApplication # importation pour PyQt6 qui permet de créer une application
from PyQt6.QtCore import Qt # importation pour PyQt6
from PyQt6.QtGui import QCursor, QIcon # importation du Cursor de PyQt6 afin d'avoir un contrôle sur ce dernier
from threading import Thread # importation du module Thread qui permet de créer et gérer des Threads

from sources.app import App # importation de l'interface graphique
from sources.packages.command import Worker, Worker4Keyboard # importation du gestionnaire des commandes
from config import NAVIGATION_MODE, APP_VERSION, OLD_APP_VERSION, APP_NAME # importation de la variable "NAVIGATION_MODE" qui permet de savoir si l'on utilise le joystick ou le clavier/souris, de la variable "APP_VERSION" pour recuperer la version de l'application, "ODL_APP_VERSION" la version precedente et "APP_NAME" le nom de l'application

# ASSERTIONS
assert APP_VERSION >= OLD_APP_VERSION , 'Error in config.py file about "APP_VERSION" and "OLD_APP_VERSION", "APP_VERSION" must be bigger than "OLD_APP_VERSION"'
assert APP_VERSION != '' , 'Please give a version to the app in config.py set for example "APP_VERSION=v0.1.0" it must be bigger than "OLD_APP_VERSION'
assert NAVIGATION_MODE == 'JOYSTICK' or NAVIGATION_MODE == 'KEYBOARD_MOUSE' , 'Error in config.py file about NAVIGATION_MODE can only be "JOYSTICK" or "KEYBOARD_MOUSE", change this setting and then restart program.'


def main():
    """
    Fonction main qui gère le lancement et la création de l'application.
    """
    app_settings = QApplication(sys.argv) # création de l'application
    app_settings.setApplicationName(f'{APP_NAME}  ({APP_VERSION})') # défini le nom de l'application
    app_settings.setWindowIcon(QIcon('./sources/content/images/icon/app_icon.svg'))
    
    app = Handler() # création la fenetre
    app.showFullScreen() # affichage en mode plein écran

    print('+==================='+ APP_NAME + '===================+')
    print('| Thread : handler         |   Statut : opérationnel   |') # affichage du statut du thread 'handler'

    if NAVIGATION_MODE == 'JOYSTICK':
        app_settings.setOverrideCursor(QCursor(Qt.CursorShape.BlankCursor)) # rend invisible le curseur de la souris dans l'application
        worker = Worker(app) # gestionnaire des commandes pour joystick
        worker.command_signal.connect(app.command_handler) # connecte les signaux du fichier command.py avec la fonction command_handler du fichier player.py
    
    if NAVIGATION_MODE == 'KEYBOARD_MOUSE':
        worker = Worker4Keyboard(app) # gestionnaire des commandes pour clavier/souris
        worker.command_signal.connect(app.command_handler) # connecte les signaux du fichier command.py avec la fonction command_handler du fichier player.py
   
    command_thread = Thread(target=worker.run) # création du thread des commandes
    command_thread.start() # lancement du thread des commandes
    
    print('+--------------------------+---------------------------+')
    print('| Thread : command         |   Statut : opérationnel   |') # affichage du statut du thread 'command'
    print('+--------------------------+---------------------------+')
    print('| Application:             |   ' + APP_NAME + '        |') # nom de l'application
    print('| Version:                 |   ' + APP_VERSION + '           |') # version de l'application
    print('| Statut:                  |   prêt                    |') # statut de l'application
    print('+======================================================+\n')
    
    sys.exit(app_settings.exec()) # execute l'application


if __name__ == '__main__':
    main() # lancement de la fonction main qui gère le lancement et la création de l'application

