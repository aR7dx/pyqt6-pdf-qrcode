# Ce fichier gère la caméra, la reconnaissance des qrcodes et la récupération de leur donnée.

import cv2 # importation du module opencv-contrib-python
# importation du module PyQt6 et de ses composants
from PyQt6.QtWidgets import QMainWindow, QLabel
from PyQt6.QtCore import QTimer, pyqtSignal
from PyQt6.QtGui import QImage, QPixmap


###############################
#### CREATION DE LA CLASSE ####
###############################


class CameraApp(QMainWindow):

    data_available = pyqtSignal(str) # déclaration d'un signal "data_available" qui émettra une chaîne de caractères lorsqu'un QR code sera détecté.

    def __init__(self):
        QMainWindow.__init__(self)
        """
        Initialisation de la classe CameraApp. Cette méthode configure l'interface graphique et initialise les paramètres de la caméra.
        """

        self.statut = False
        
        self.setWindowTitle('CameraApp')

        self.lecteur_video = QLabel()
        self.setCentralWidget(self.lecteur_video)

        self.camera = cv2.VideoCapture(0)
        self.detector = cv2.QRCodeDetector()
        _, img = self.camera.read()
        self.hauteur_video, self.largeur_video, _ = img.shape

        # Un timer est configuré pour appeler périodiquement la fonction scan pour détecter les QR codes.
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.scan)
        self.data = None

    def __repr__(self):
        return str('CameraApp')


    #################################
    #### CREATIONS DES FONCTIONS ####
    #################################
        

    def start_camera(self, callback):
        """
        Méthode pour démarrer la caméra. Elle démarre le timer pour commencer la capture vidéo et connecte le signal data_available à une fonction de rappel spécifiée.
        """
        self.timer.start(30)
        self.data_available.connect(callback)

    def scan(self):
        """
        Cette méthode scanne les images provenant de la caméra. Elle crée un objet QImage à partir de cette image pour l'afficher dans l'interface graphique.
        Ensuite, elle détecte les QR codes dans l'image. Si un QR code est détecté, les données sont émises via le signal "data_available".
        """
        self.statut = True
        
        ret, frame = self.camera.read()

        if ret:
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = rgb_image.shape
            bytes_per_line = channel * width
            q_image = QImage(rgb_image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)

            self.lecteur_video.setPixmap(pixmap)

            data, bbox, _ = self.detector.detectAndDecode(frame)
        
            if(bbox is not None):
                # affiche le carré bleu autour de qrcode
                for i in range(len(bbox)):
                    cv2.line(frame, tuple(map(int, bbox[i][0])), tuple(map(int, bbox[(i+1) % len(bbox)][0])), color=(255, 0, 0), thickness=2)
                
                if data:
                    self.data = data
                    self.data_available.emit(data)
                    

    def closeEvent(self, event):
        """
        Cette méthode est appelée lorsque l'application se ferme. Elle arrête la capture vidéo de la caméra.
        """
        self.camera.release()
        event.accept()

    def get_data(self):
        """
        Méthode pour obtenir les données du dernier QR code détecté.
        """
        return self.data
    
    
