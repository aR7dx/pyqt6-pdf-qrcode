# Ce fichier contient l'interface graphique de l'application

import pynput # importation du module pynput
from pynput.keyboard import Key
from PyQt6.QtWidgets import QMainWindow, QTabWidget, QToolBar # importation des composants du module PyQt6
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView # composant du module PyQt6 qui créer un moteur de rendu pour les fichers html et pdf

from sources.packages.file import File # composant pour créer un objet fichier
from sources.packages.camera import CameraApp # composant qui gère les qrcodes
from sources.packages.videoPlayer import VideoPlayer # composant qui gère les vidéos
from config import SCROLL_SPEED, SUPPORTED_DOCUMENT_EXTENSIONS, SUPPORTED_VIDEO_EXTENSIONS
assert SCROLL_SPEED > 0, 'Veuillez fournir une valeur supérieur à zéro.'

keyboard = pynput.keyboard.Controller() # creation d'un objet pour le clavier
mouse = pynput.mouse.Controller() # creation d'un objet pour la souris

############################
#### CREATION DE CLASSE ####
############################

# utilisation de la programmation orienté objet (POO)
# creation de la fenêtre
class App(QMainWindow): # création de la classe (fenêtre)
    def __init__(self):
        super().__init__()

        self.tabs = {}
        
        self.tabMenu = QTabWidget(self) # création du Widget des onglets
        self.setCentralWidget(self.tabMenu) # défini la barre d'onglet comme element central de la fenetre
        self.tabMenu.setDocumentMode(True) # supprime le cadre blanc autour des pages
        self.tabMenu.setTabsClosable(False) # autorise la fermeture des onglets

        self.toolbar = QToolBar() # Création de la toolbar
        self.toolbar.setMovable(False) # empêche de pouvoir déplacer la toolbar
        self.toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon) # met le texte a côté du l'icone qui lui est associée
        self.toolbar.setFixedSize(500, 30) # défini la taille de la ToolBar
        self.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.toolbar) # ajout de la ToolBar sur la fenêtre et la place en pied de page

        # Création des QActions ("texte d'affichage") qui iront dans la QToolBar
        self.toolbar.addAction(QIcon('./sources/content/images/icon/joystick.png'), 'Navigation')
        self.toolbar.addAction(QIcon('./sources/content/images/icon/button_vert.png'), 'Intéragir')
        self.toolbar.addAction(QIcon('./sources/content/images/icon/button_bleu.png'), 'Scanner QR-Code')
        self.toolbar.addAction(QIcon('./sources/content/images/icon/button_rouge.png'), 'Retour')

        self.add_tab('index.html') # page d'accueil au demarrage de l'application
        self.default_style() # applique le style css pour la toolbar

    def __repr__(self): # representation de la classe
        return str(self.tabs) #on affiche la liste des pages dans le dico

    #################################
    #### CREATIONS DES FONCTIONS ####
    #################################

    def startCamera(self, label='Scanner'):
        self.scanner = CameraApp() # créer une variable qui corresond à la caméra
        self.scanner.start(self.stopCamera) # lance la fonction qui gère la caméra et renvoie la sortie sur la fonction stopCamera

        i = self.tabMenu.addTab(self.scanner, label)
        self.tabMenu.setCurrentIndex(i)

    def stopCamera(self, data):
        self.close_tab() # ferme l'onglet de la caméra et l'arrête par conséquent
        self.add_tab(data) # la data vers la fonction add_tab

    def add_tab(self, data):
        """
        Fonction permettant l'ajout de nouveaux onglets
        """
        file = File(str(data)) # creer un objet de type File

        # on verifie si le fichier cible existe
        if file.isExisting() == False: 
            return

        self.tabs[file.name] = file.path # creer un clé et une valeur pour le fichier dans le dico tabs
            
        def createBrowser(file, label='chargement...'):
            browser = QWebEngineView() # creation de la partie graphique "moteur de rendu" qui affichera les fichiers ouverts
            # paramètrage afin de supporter les documents pdf
            browser.settings().setAttribute(browser.settings().WebAttribute.PluginsEnabled, True) # autorisarion des plugins dans le moteur de rendu
            browser.settings().setAttribute(browser.settings().WebAttribute.PdfViewerEnabled, True) # autorisation des fichiers pdf dans le moteur de rendu
            browser.setUrl(QUrl.fromLocalFile(file.path)) # ajoute la page avec l'url/fichier renseigner
            
            i = self.tabMenu.addTab(browser, label) # attribut l'onglet actuel à une variable
            self.tabMenu.setCurrentIndex(i) # fixe l'indice de l'onglet
            
            browser.loadFinished.connect(lambda _, i=i, browser=browser: self.tabMenu.setTabText(i, browser.page().title()))
            
        def createPlayer(file, label='Lecteur Video'):
            self.videoTab = VideoPlayer() # créer l'objet VideoPlayer qui est le lecteur vidéo
            self.videoTab.play(file) # lance la lecture du fichier vidéo
            
            i = self.tabMenu.addTab(self.videoTab, label) # attribut l'onglet actuel à une variable
            self.tabMenu.setCurrentIndex(i) # fixe l'indice de l'onglet
        
        # Aberration 
        # (decide si il faut créer une page pour un fichier ou un lecteur pour une vidéo)
        # renvoi un message si l'extension du fichier est inconnu du logiciel
        [createBrowser(file) if len([x for x in SUPPORTED_DOCUMENT_EXTENSIONS if x == file.ext]) > 0 else [createPlayer(file) if len([x for x in SUPPORTED_VIDEO_EXTENSIONS if x == file.ext]) > 0 else print(f'\nLe fichier "{file.name}" n\'existe pas !\n')]]

    def close_tab(self):
        """
        Permet de fermer un onglet.
        """
        try: # si l'objet caméra existe
            self.scanner.close() # on l'arrete
            del self.scanner # on le supprime
        except AttributeError:
            pass
        
        try:
            self.videoTab.stop() # arrete le lecteur video, si une vidéo est entrain d'être jouée
        except AttributeError:
            pass
        
        if self.tabMenu.count() < 2: # Garde au moins un onglet ouvert
            return # ne retourne rien pour faire aucune action et ne pas arreter le programme

        # supprime une fenetre
        current_tab_index = self.tabMenu.currentIndex() # recupere l'indice de l'onglet actuel
        self.tabMenu.removeTab(current_tab_index) # supprime l'onglet actuel
    
    ################################
    #### GESTIONS DES COMMANDES ####
    ################################     

    # Programmation Evenementielle
    # Les actions proviennent du fichier command.py suite à l'activation d'un bouton ou du joystick
    
    def command_handler(self, command):
        """
        Fonction qui détecte lorsque qu'une touche spécifique est pressée ou qu'une action précise est réalisée.
        """
        if command == 'z': # on monte la page vers le haut (scroll vers le haut)
            mouse.scroll(0,SCROLL_SPEED) # if dont work replace the line by 'keyboard.tap(Key.up)'
        elif command == 's': # on descend la page (scroll vers le bas)
            mouse.scroll(0,-SCROLL_SPEED) # if dont work replace the line by 'keyboard.tap(Key.down)'
        elif command == 'q': # déplace le curseur sur la gauche pour passer au bouton précédent
            keyboard.press(Key.shift)
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            keyboard.release(Key.shift)
        elif command == 'd': # déplace le curseur sur la droite pour passer au bouton suivant
            keyboard.tap(Key.tab)
        elif command == 'x': # presse la touche entrer pour valider une action
            keyboard.tap(Key.enter)
        elif command == 'b': # supprime l'onglet actif
            self.close_tab()
        elif command == 'c': # active la caméra
            self.startCamera()
        elif command == 'w': # quitte l'application
            self.close()
            print('/!\ Vous venez de quitter l\'application.')
            print('/!\ Veuillez fermer ce terminal.')
            print("\n/!\ Ne pas tenir compte de l'erreur ci-dessous.\n")
            raise Exception('Vous venez de quitter l\'application.')

    def default_style(self):
        """
        Style CSS sur l'application concerne la toolbar.
        """
        self.setStyleSheet('''
            QWidget{
                background-color: rgb(24,24,24);
                border-color: transparent;
                color: #f2f2f9;
            }
            QTabBar::tab{
                background: black;
                border-top-left-radius: 7px;
                border-top-right-radius: 7px;
                padding: 1px 6px 2px 6px;
                margin-right: 1.5px;
            }
            QTabBar::tab:selected {
                border: 2px solid rgb(169, 173, 197);
            }
            QTabBar::tab:!selected {
                margin-top: 3px;
                border: 1.5px solid rgba(160, 160, 160, 0.9);
            }
                            ''')

