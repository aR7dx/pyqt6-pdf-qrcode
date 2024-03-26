# Ce fichier est le gestionaire de commande de l'application, centralise tout les requêtes de commande de l'application issue de la programmation evenementielle 

from PyQt6.QtCore import QObject, pyqtSignal  # importation du module PyQt6 et des ses composants
import serial # importation du module serial pour détecter et utiliser la trame des ports usb de la raspberry 4 pour le fonctionnement du joystick
import keyboard # importation du module keyboard qui sert a récupérer un input du clavier
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



# Seconde classe qui permet d'altérner entre un joystick et un clavier/souris      
      
class Worker4Keyboard(QObject): # création du gestionnaire de commande
  command_signal = pyqtSignal(str) # variable qui permet la reception du signal apres émission de celui-ci

  def __init__(self, window_instance):
    super().__init__()
    self.window_instance = window_instance # création une instance de la classe

  def run(self): # fonction qui s'execute lors de l'activation du thread
    while True:
  
      if keyboard.is_pressed('q'): # si la touche q est actionnée
        self.command_signal.emit('q') # on emet le signal 'q' pour signifier que l'on appuie sur la touche q, afin de passer au bouton précédent
 
      elif keyboard.is_pressed('d'): # si la touche d est actionnée
        self.command_signal.emit('d') # on emet le signal 'd' pour signifier que l'on appuie sur la touche d, afin de passer au bouton suivant

      elif keyboard.is_pressed('f'): # si la touche f est actionnée
        self.command_signal.emit('f') # on emet le signal 'f' pour signifier que l'on appuie sur la touche f, cela permet d'activer la caméra afin de scanner un qrcode sans passer par les boutons qui sont sur les pages

      elif keyboard.is_pressed('x'): # si la touche x est actionnée
        self.command_signal.emit('x') # on emet le signal 'x' pour signifier que l'on appuie sur la touche x, cela permet de séléctionner/valider une action

      elif keyboard.is_pressed('b'): # si la touche b est actionnée
        self.command_signal.emit('b') # on emet le signal 'b' pour signifier que l'on appuie sur la touche b, cela permet de faire un retour en arrière lorsque cela est possible
        
      elif keyboard.is_pressed('e'): # si la touche e est actionnée
        self.command_signal.emit('e') # on emet le signal 'e' pour signifier que l'on appuie sur la touche e, cela permet de quitter l'application en provoquant une erreur dans l'application, ce qui interrompt le programme
      
      sleep(0.1) # "temps de pause" entre les actions des boutons et du joystick
