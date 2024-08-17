# ce fichier gère la lecture des vidéos via un lecteur intégré

from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QVBoxLayout, QWidget

class VideoPlayer(QWidget):
  def __init__(self, parent=None):
    super(VideoPlayer, self).__init__(parent)
    """
      Initialisation de la classe VideoPlayer. Cette méthode configure les composants audio et vidéo et créer une surface pour afficher la vidéo.
    """
    
    self.mediaPlayer = QMediaPlayer(self)
    self.video = QVideoWidget(self)
    
    self.audio = QAudioOutput(self)
    self.mediaPlayer.setAudioOutput(self.audio) # defini la sortie audio du lecteur de video
    self.mediaPlayer.setVideoOutput(self.video) # defini la sotie video du lecteur de video
    
    layout = QVBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0) # retire le cadre autour de la video
    layout.addWidget(self.video)
    
    self.setLayout(layout) # applique le layout sur l'objet
  
  def play(self, page):
    self.mediaPlayer.setSource(QUrl.fromLocalFile(page.path)) # charge le fichier a partir de son chemin d'emplacement
    self.audio.setVolume(0.8) # volume du lecteur de video
    self.mediaPlayer.play() # joue le contenu du lecteur video
    
  def stop(self):
    self.mediaPlayer.stop() # arrete le contenu du lecteur video
