# Ce fichier est le gestionaire de commande de l'application, centralise tout les requêtes de commande de l'application issue de la programmation evenementielle 

from PyQt6.QtCore import QObject, pyqtSignal  # importation du module PyQt6 et des ses composants
import serial # importation du module serial pour détecter et utiliser la trame des ports usb de la raspberry 4 pour le fonctionnement du joystick
from pynput import keyboard # importation du module pynput qui sert a récupérer un input du clavier
from time import sleep # importation du module sleep qui permet de faire des "temps de pause" dans le code

class Worker(QObject): # création du gestionnaire de commande
  command_signal = pyqtSignal(str) # variable qui permet la reception du signal apres émission de celui-ci

  def __init__(self, window_instance):
    super().__init__()
    self.window_instance = window_instance # création une instance de la classe

  def run(self):
    """
    Fonction qui s'execute lors de l'activation du thread.
    """
    portSerie = serial.Serial("/dev/ttyACM0") # port sur lequel la trame entre le joystick et la carte ce fait
    
    while True:
      trame = portSerie.readline() # on lit la trame du port souhaité
      message=trame.decode('utf8') # on précise que le message sera décodé en utf8
      donnees = message.split(',') # on utilise la virgule comme séparateur entre les informations de la trame
      
      if donnees[5] == 'haut':
        self.command_signal.emit('z') # signal 'z' joystick vers le haut
      elif donnees[5] == 'bas':
        self.command_signal.emit('s') # signal 's' joystick vers le bas
      elif donnees[5] == 'gauche':
        self.command_signal.emit('q') # signal 'q'  joystick vers le gauche
      elif donnees[5] == 'droite':
        self.command_signal.emit('d') # signal 'd' joystick vers le droite
      elif donnees[4] == 'True':
        self.command_signal.emit('c') # signal 'c' active la caméra
      elif donnees[3] == 'True':
        self.command_signal.emit('x') # signal 'x' séléctionne/valide une action
      elif donnees[2] == 'True':
        self.command_signal.emit('b') # signal 'b' retour en arrière lorsque cela est possible
      elif donnees[1] == 'True':
        self.command_signal.emit('w') # signal 'w' quitte l'application 
      
      sleep(0.1) # "temps de pause" entre les actions



# Seconde classe qui permet d'altérner entre un joystick et un clavier/souris      
      
class Worker4Keyboard(QObject): # création du gestionnaire de commande
  command_signal = pyqtSignal(str) # variable qui permet la reception du signal apres émission de celui-ci

  def __init__(self, window_instance):
    super().__init__()
    self.window_instance = window_instance # création une instance de la classe
    self.key_state = {
        'c': False, # signal 'c' active la caméra
        'b': False, # signal 'b' retour en arrière lorsque cela est possible
        'w': False # signal 'w' quitte l'application
    }
    self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
    self.listener.start()

  def on_press(self, key):
    try:
      if key.char in self.key_state:
        self.key_state[key.char] = True
    except AttributeError:
      pass

  def on_release(self, key):
    try:
      if key.char in self.key_state:
        self.key_state[key.char] = False
    except AttributeError:
      pass

  def run(self):
    """
    Fonction qui s'execute lors de l'activation du thread.
    """
    while True:
      for key, pressed in self.key_state.items():
        if pressed:
          self.command_signal.emit(key)
          sleep(2)
          break
      else:
        sleep(0.1) # évite une surcharge de signaux
