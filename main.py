# fichier principal/central du programme: son rôle est d'ordonner la création des différents composants de l'application.

import sys # importation du module sys
from PyQt6.QtWidgets import QApplication # importation pour PyQt6 qui permet de créer une application
from threading import Thread # importation du module Thread qui permet de créer et gérer des Threads
from window import Window # importation de l'interface graphique
from command import Worker # importation du gestionnaire des commandes


def main(): # création de la fonction main qui gère le lancement et la création de l'application
    app = QApplication(sys.argv) # création de l'application
    app.setOverrideCursor(QCursor(Qt.CursorShape.BlankCursor)) # rend invisible le curseur dans l'application
    app.setApplicationName('Scanner Qrcode Application') # défini le nom de l'application
    
    win = Window() # création la fenetre
    win.show() # affichage en mode plein écran
    print('Thread : window           |   Statut : opérationnel') # affichage du statut du thread 'window'
    
    worker = Worker(win) # gestionnaire des commandes
    worker.command_signal.connect(win.command_handler) # connexion/lien/pont avec le gestionnaire des commandes
    
    command_thread = Thread(target=worker.run) # création du thread des commandes
    command_thread.start() # lancement du thread des commandes
    print('Thread : command_thread   |   Statut : opérationnel') # affichage du statut du thread 'command'
    
    print('=====') # séparateur
    print('Application chargée !') # statut de l'application
    print('version: v0.1.0-beta') # version de l'application
    print('=====') # séparateur
    
    sys.exit(app.exec()) # execute l'application


if __name__ == '__main__':
    main() # lancement de la fonction main qui gère le lancement et la création de l'application

