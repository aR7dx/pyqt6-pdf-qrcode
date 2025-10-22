# Ce fichier gère la caméra, la reconnaissance des qrcodes et la récupération de leur donnée.

import cv2 # importation du module opencv-contrib-python
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import QTimer, pyqtSignal, Qt
from PyQt6.QtGui import QImage, QPixmap

###############################
#### CREATION DE LA CLASSE ####
###############################

class CameraApp(QWidget):

    data_available = pyqtSignal(str) # déclaration d'un signal "data_available" qui émettra une chaîne de caractères lorsqu'un QR code sera détecté.

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        """
        Initialisation de la classe CameraApp. Cette méthode configure l'interface graphique et initialise les paramètres de la caméra.
        """

        self.statut = False
        self.data = None

        self.camera = cv2.VideoCapture(0)
        self.detector = cv2.QRCodeDetector()
        self.lecteur_cam = QLabel()

        self.lecteur_cam.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0) # retire le cadre autour de la camera
        layout.addWidget(self.lecteur_cam)
        
        self.setLayout(layout)

        self.timer = QTimer(self) # Un timer est configuré pour appeler périodiquement la fonction scan pour détecter les QR codes.
        self.timer.timeout.connect(self.scan)

    def __repr__(self):
        return str('CameraApp')


    #################################
    #### CREATIONS DES FONCTIONS ####
    #################################
        

    def start(self, callback):
        """
        Méthode pour démarrer la caméra. Elle démarre le timer pour commencer la capture vidéo et connecte le signal data_available à une fonction de rappel spécifiée.
        """
        self.timer.start(30)
        self.data_available.connect(callback)

    def scan(self):
        
        self.statut = True # Mise à jour de l'état pour indiquer que la caméra est active.
        
        ret, frame = self.camera.read()
        # Capture une image de la caméra. 'ret' est un indicateur de succès (True si l'image a été capturée avec succès, False sinon).
        # 'frame' contient l'image capturée.

        if ret: # Vérifie si la capture d'image a réussi.
            
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Convertit l'image de l'espace de couleurs BGR (utilisé par OpenCV) en espace de couleurs RGB (utilisé par PyQt6).
            height, width, channel = rgb_image.shape # Récupère les dimensions de l'image: hauteur, largeur et nombre de canaux de couleur (3 pour RGB).
            
            bytes_per_line = channel * width # Calcule le nombre d'octets par ligne dans l'image. Nécessaire pour créer un objet QImage.
            
            q_image = QImage(rgb_image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888) # Crée un objet QImage à partir des données de l'image RGB.
            pixmap = QPixmap.fromImage(q_image) # Convertit l'objet QImage en QPixmap
            
            self.lecteur_cam.setPixmap(pixmap) # Met à jour l'affichage du QLabel avec la nouvelle image capturée et traitée.

            data, bbox, _ = self.detector.detectAndDecode(frame)
            # Utilise le détecteur de QR code pour détecter et décoder les QR codes dans l'image capturée.
            # 'data' contient les données du QR code si un QR code est détecté.
            # 'bbox' contient les coordonnées de la surface englobant le QR code détecté.
        
            if(bbox is not None): # Vérifie si un QR code a été détecté
                if data: # Vérifie si des données ont été extraites du QR code.
                    self.data = data # Met à jour l'attribut 'data' avec les données du QR code détecté.
                    self.data_available.emit(data) # Émet le signal 'data_available' avec les données du QR code.
                    

    def closeEvent(self, event):
        """
        Cette méthode est appelée lorsque l'application se ferme. Elle arrête la capture vidéo de la caméra.
        """
        self.camera.release()
        event.accept()
    
    
