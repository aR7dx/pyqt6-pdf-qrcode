import cv2
# importation du module PyQt6
from PyQt6.QtWidgets import QMainWindow, QLabel
from PyQt6.QtCore import Qt, QTimer, pyqtSignal
from PyQt6.QtGui import QImage, QPixmap




###############################
#### CREATION DE LA CLASSE ####
###############################




class CameraApp(QMainWindow):

    data_available = pyqtSignal(str)

    def __init__(self):
        QMainWindow.__init__(self)
        
        self.setWindowTitle('CameraApp')

        self.lecteur_video = QLabel()
        self.setCentralWidget(self.lecteur_video)

        self.camera = cv2.VideoCapture(0)
        self.detector = cv2.QRCodeDetector()
        _, img = self.camera.read()
        self.hauteur_video, self.largeur_video, _ = img.shape

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.scan)
        self.data = None




    #################################
    #### CREATIONS DES FONCTIONS ####
    #################################
        



    def start_camera(self, callback):
        self.timer.start(30)
        self.data_available.connect(callback)

    def scan(self):
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
        # Arrete la camera lorsque l'on ferme l'application
        self.camera.release()
        event.accept()
        
    def keyPressEvent(self, event):
        if (event.key() == Qt.Key.Key_B):
            self.data_available.emit(None) # si la touche B est pressée cela arrete le programme car on renvoi None

    def get_data(self):
        return self.data
    
    
