# fichier principal/central du programme: son rôle est d'ordonner la création des différents composants de l'application.

import os # importation du module os
import sys # importation du module sys
from PyQt6.QtWidgets import QApplication # importation pour PyQt6 qui permet de créer une application
from PyQt6.QtCore import Qt # importation pour PyQt6
from PyQt6.QtGui import QCursor # importation du Cursor de PyQt6 afin d'avoir un contrôle sur ce dernier
from threading import Thread # importation du module Thread qui permet de créer et gérer des Threads
from window import Window # importation de l'interface graphique
from command import Worker, Worker4Keyboard # importation du gestionnaire des commandes

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # trouve le chemin absolu du fichier, et os.path.dirname() l'appelle une seconde fois pour obtenir le chemin du dossier parent. Ensuite, ce chemin est ajouté à sys.path, ce qui permet à Python de trouver et d'importer le module config.

from config import NAVIGATION_MODE, APP_VERSION, OLD_APP_VERSION # importation de la variable "NAVIGATION_MODE" qui permet de savoir si l'on utilise le joystick ou le clavier/souris et de la variable "APP_VERSION" pour recuperer la version de l'application et "ODL_APP_VERSION" la version precedente

if (APP_VERSION > OLD_APP_VERSION) != True:
    raise Exception('Error in config.py file about "APP_VERSION" and "OLD_APP_VERSION", "APP_VERSION" must be bigger than "OLD_APP_VERSION" or it would makes no sense.')



def main(): # création de la fonction main qui gère le lancement et la création de l'application
    app = QApplication(sys.argv) # création de l'application
    app.setOverrideCursor(QCursor(Qt.CursorShape.BlankCursor)) # rend invisible le curseur dans l'application
    app.setApplicationName('pyqt6-pdf-qrcode') # défini le nom de l'application
    
    win = Window() # création la fenetre
    win.show() # affichage en mode plein écran
    print('Thread : window           |   Statut : opérationnel') # affichage du statut du thread 'window'

    if NAVIGATION_MODE == 'JOYSTICK':
        worker = Worker(win) # gestionnaire des commandes
        worker.command_signal.connect(win.command_handler) # connexion/lien/pont avec le gestionnaire des commandes
    elif NAVIGATION_MODE == 'KEYBOARD_MOUSE':
        worker = Worker4Keyboard(win)
        worker.command_signal.connect(win.command_handler)
    else:
        raise Exception('Error in config.py file about NAVIGATION_MODE can only be "JOYSTICK" or "KEYBOARD_MOUSE", change this setting and then restart program.')
    
    command_thread = Thread(target=worker.run) # création du thread des commandes
    command_thread.start() # lancement du thread des commandes
    print('Thread : command_thread   |   Statut : opérationnel') # affichage du statut du thread 'command'
    
    print('=====') # séparateur
    print('Application chargée !') # statut de l'application
    print('version: ' + APP_VERSION) # version de l'application
    print('=====') # séparateur
    
    sys.exit(app.exec()) # execute l'application


if __name__ == '__main__':
    main() # lancement de la fonction main qui gère le lancement et la création de l'application

