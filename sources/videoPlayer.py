from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QVBoxLayout, QWidget

from config import VIDEOPLAYER_VOLUME # variable du volume du lecteur de video

class VideoPlayer(QWidget):
  def __init__(self, parent=None):
    super(VideoPlayer, self).__init__(parent)
    
    self.mediaPlayer = QMediaPlayer(self)
    self.video = QVideoWidget(self)
    
    self.audio = QAudioOutput(self)
    self.mediaPlayer.setAudioOutput(self.audio) # defini la sortie audio du lecteur de video
    self.mediaPlayer.setVideoOutput(self.video) # defini la sotie video du lecteur de video
    
    layout = QVBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0) # retire le cadre autour de la video
    layout.addWidget(self.video)
    
    self.setLayout(layout)
  
  def play(self, page):
    self.mediaPlayer.setSource(QUrl.fromLocalFile(page.url)) # charge le fichier a partir de son chemin d'emplacement
    self.audio.setVolume(VIDEOPLAYER_VOLUME) # volume du lecteur de video
    self.mediaPlayer.play()
    
  def stop(self):
    self.mediaPlayer.stop()