# fichier principal/central du programme: son rôle est d'ordonner la création des différents composants de l'application.

import sys # importation du module sys
from PyQt6.QtWidgets import QApplication # importation pour PyQt6 qui permet de créer une application
from PyQt6.QtCore import Qt # importation pour PyQt6
from PyQt6.QtGui import QCursor, QIcon # importation du Cursor de PyQt6 afin d'avoir un contrôle sur ce dernier
from threading import Thread # importation du module Thread qui permet de créer et gérer des Threads
from window import Window # importation de l'interface graphique
from command import Worker, Worker4Keyboard # importation du gestionnaire des commandes

from config import NAVIGATION_MODE, APP_VERSION, OLD_APP_VERSION, APP_NAME # importation de la variable "NAVIGATION_MODE" qui permet de savoir si l'on utilise le joystick ou le clavier/souris, de la variable "APP_VERSION" pour recuperer la version de l'application, "ODL_APP_VERSION" la version precedente et "APP_NAME" le nom de l'application

# ASSERTIONS
assert APP_VERSION >= OLD_APP_VERSION , 'Error in config.py file about "APP_VERSION" and "OLD_APP_VERSION", "APP_VERSION" must be bigger than "OLD_APP_VERSION"'
assert APP_VERSION != '' , 'Please give a version to the app in config.py set for example "APP_VERSION=v0.1.0" it must be bigger than "OLD_APP_VERSION'
assert NAVIGATION_MODE == 'JOYSTICK' or NAVIGATION_MODE == 'KEYBOARD_MOUSE' , 'Error in config.py file about NAVIGATION_MODE can only be "JOYSTICK" or "KEYBOARD_MOUSE", change this setting and then restart program.'


def main():
    """
    Fonction main qui gère le lancement et la création de l'application.
    """
    app = QApplication(sys.argv) # création de l'application
    app.setApplicationName(f'{APP_NAME}  ({APP_VERSION})') # défini le nom de l'application
    app.setWindowIcon(QIcon('./sources/images/icon/app_icon.svg'))

    app.setOverrideCursor(QCursor(Qt.CursorShape.BlankCursor)) # rend invisible le curseur de la souris dans l'application
    
    win = Window() # création la fenetre
    win.showFullScreen() # affichage en mode plein écran

    print('+==================='+ APP_NAME + '===================+')
    print('+--------------------------+---------------------------+')
    print('| Thread : window          |   Statut : opérationnel   |') # affichage du statut du thread 'window'

    if NAVIGATION_MODE == 'JOYSTICK':
        worker = Worker(win) # gestionnaire des commandes
        worker.command_signal.connect(win.command_handler) # connexion/lien/pont avec le gestionnaire des commandes
    
    if NAVIGATION_MODE == 'KEYBOARD_MOUSE':
        app.setOverrideCursor(QCursor(Qt.CursorShape.ArrowCursor)) # affiche le curseur de la souris
        worker = Worker4Keyboard(win)
        worker.command_signal.connect(win.command_handler)
   
    command_thread = Thread(target=worker.run) # création du thread des commandes
    command_thread.start() # lancement du thread des commandes
    print('| Thread : command_thread  |   Statut : opérationnel   |') # affichage du statut du thread 'command'
    
    print('+--------------------------+---------------------------+') # séparateur
    print('| Application:             |   ' + APP_NAME + '        |') # nom de l'application
    print('| Statut:                  |   prêt                    |') # statut de l'application
    print('| version:                 |   ' + APP_VERSION + '           |') # version de l'application
    print('+------------------------------------------------------+') # séparateur
    
    sys.exit(app.exec()) # execute l'application


if __name__ == '__main__':
    main() # lancement de la fonction main qui gère le lancement et la création de l'application

