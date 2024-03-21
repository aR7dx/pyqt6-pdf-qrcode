from PyQt6.QtCore import QObject, pyqtSignal
import serial
from time import sleep



class Worker(QObject):
  command_signal = pyqtSignal(str)

  def __init__(self, window_instance):
    super().__init__()
    self.window_instance = window_instance

  def run(self):
    portSerie = serial.Serial("/dev/ttyACM0")
    
    while True:
      trame = portSerie.readline()
      message=trame.decode('utf8')
      donnees = message.split(',')
      
      if donnees[5] == 'haut':
        self.command_signal.emit('z')
      
      elif donnees[5] == 'bas':
        self.command_signal.emit('s')
      
      elif donnees[5] == 'gauche':
        self.command_signal.emit('q')

      elif donnees[5] == 'droite':
        self.command_signal.emit('d')

      elif donnees[4] == 'True':
        self.command_signal.emit('f')

      elif donnees[3] == 'True':
        self.command_signal.emit('x')

      elif donnees[2] == 'True':
        self.command_signal.emit('b')
        
      elif donnees[1] == 'True':
        self.command_signal.emit('e')
      
      sleep(0.1)
