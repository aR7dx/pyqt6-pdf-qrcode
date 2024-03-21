# Ce fichier est le gestionaire de commande de l'application, centralise tout les requêtes de commande de l'application issue de la programmation evenementielle 

from PyQt6.QtCore import QObject, pyqtSignal  # importation du module PyQt6 et des ses composants
import serial # importation du module serial pour détecter et utiliser la trame des ports usb de la raspberry 4 pour le fonctionnement du joystick
from time import sleep # importation du module sleep qui permet de faire des "temps de pause" dans le code



class Worker(QObject): # création du gestionnaire de commande
  command_signal = pyqtSignal(str) # variable qui permet la reception du signal apres émission de celui-ci

  def __init__(self, window_instance):
    super().__init__()
    self.window_instance = window_instance # création une instance de la classe

  def run(self): # fonction qui s'execute lors de l'activation du thread
    portSerie = serial.Serial("/dev/ttyACM0") # port sur lequel la trame entre le joystick et la carte ce fait
    
    while True:
      trame = portSerie.readline() # on lit la trame du port souhaité
      message=trame.decode('utf8') # on précise que le message sera décodé en utf8
      donnees = message.split(',') # on utilise la virgule comme séparateur entre les informations de la trame
      
      if donnees[5] == 'haut':  # joystick vers le haut
        self.command_signal.emit('z') # on emet le signal 'z' pour signifier que le joystick est vers le haut
      
      elif donnees[5] == 'bas': # joystick vers le bas
        self.command_signal.emit('s') # on emet le signal 's' pour signifier que le joystick est vers le bas
      
      elif donnees[5] == 'gauche': # joystick vers le gauche
        self.command_signal.emit('q') # on emet le signal 'q' pour signifier que le joystick est vers le gauche

      elif donnees[5] == 'droite': # joystick vers le droite
        self.command_signal.emit('d') # on emet le signal 'd' pour signifier que le joystick est vers le droite

      elif donnees[4] == 'True': # signal correspondant au bouton bleu de notre boîte
        self.command_signal.emit('f') # on emet le signal 'f' pour signifier que le bouton bleu est actionné, cela permet d'activer la caméra afin de scanner un qrcode sans passer par les boutons qui sont sur les pages

      elif donnees[3] == 'True': # signal correspond au bouton vert de notre boîte
        self.command_signal.emit('x') # on emet le signal 'x' pour signifier que le bouton vert est actionné, cela permet de séléctionner/valider une action

      elif donnees[2] == 'True': # signal correspond au bouton rouge de notre boîte
        self.command_signal.emit('b') # on emet le signal 'b' pour signifier que le bouton rouge est actionné, cela permet de faire un retour en arrière lorsque cela est possible
        
      elif donnees[1] == 'True': # signal correspond au bouton noir de notre boîte
        self.command_signal.emit('e') # on emet le signal 'e' pour signifier que le bouton noir est actionné, cela permet de quitter l'application en provoquant une erreur, ce qui va interrompt le programme
      
      sleep(0.1) # "temps de pause" entre les actions des boutons et du joystick
