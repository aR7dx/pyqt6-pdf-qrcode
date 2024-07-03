# Ce fichier permet de créer un objet fichier auquel s'applique différentes méthodes

import os

class File():
  def __init__(self, name):
    self.name = name # nom du fichier cible
    self.ext = None # extension du fichier cible
    self.dir = None # chemin du dossier du fichier cible
    self.path = None # chemin du fichier cible
    
    self.createPath()
      
  def __repr__(self):
    return str(self.name)
  
  def __str__(self):
    return str(self.name) + ', ' + str(self.path)
  
  def isExisting(self):
    for _, _, file in os.walk(self.dir):
      if self.name in file:
        return True
    print(f'\nLe fichier {self.name} n\'existe pas !\n')
    return False

  def createPath(self):
    self.ext = (self.name).split('.')[-1]
    self.dir = os.path.split(os.path.abspath(__file__))[0]+r'/../content/' + str(self.ext) + "/"
    self.path = str(self.dir) + str(self.name)
