import sys
from PyQt6.QtWidgets import QApplication
from threading import Thread
from window import Window
from command import Worker


def main():
    app = QApplication(sys.argv) # creation de l'application
    app.setApplicationName('Scanner Qrcode Application') # défini le nom de l'application
    
    win = Window() # création la fenetre
    win.show() # affichage en mode plein écran
    print('Thread : window           |   Statut : opérationnel')
    
    worker = Worker(win)
    worker.command_signal.connect(win.command_handler)
    
    command_thread = Thread(target=worker.run)
    command_thread.start()
    print('Thread : command_thread   |   Statut : opérationnel')
    
    # changer la version quand il y a des changements assez importants ou nouvelles fontionnalitées
    print('=====')
    print('Application chargée !')
    print('version: v1.2')
    print('=====')
    
    sys.exit(app.exec()) # execute l'application


if __name__ == '__main__':
    main()

