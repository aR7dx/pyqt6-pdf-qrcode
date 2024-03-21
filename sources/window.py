# Ce fichier contient l'interface graphique de l'application

import sys # importation du module sys
import os  # importation du module os
import pyautogui # importation du module pyautogui pour effectuer des actions graphiques notamment

# importation des composants du module PyQt6
from PyQt6.QtWidgets import QMainWindow, QTabWidget, QToolBar
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtWebEngineWidgets import QWebEngineView # composant du module PyQt6 qui créer un moteur de rendu pour les fichers html et pdf
from scan_qrcode import CameraApp # composant qui gère les qrcodes

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # trouve le chemin absolu du fichier, et os.path.dirname() l'appelle une seconde fois pour obtenir le chemin du dossier parent. Ensuite, ce chemin est ajouté à sys.path, ce qui permet à Python de trouver et d'importer le module config.

from config import SCROLL_SPEED # importation de la variable "SCROLL_SPEED" qui permet de savoir si la vitesse de defilement sur une page

pyautogui.PAUSE = 0 # variable du module pyautogui qui permet de choisir le délai entre chaque action du module
listeAccueil = [(330,900),(1540,100),(1750,100)] # coordonnées de la page d'accueil
listeCrédits = [(1540,100),(1750,100)] # coordonnées de la page des crédits
listeSelection = [(760,615),(1170,615)] # coordonnées de la page de séléction
j = 0 # compteur (sert pour savoir quel action effectuer)
data_file = None # donnée récupérée par la caméra



###############################
#### CREATION DE LA CLASSE ####
###############################


# utilisation de la programmation orienté objet (POO)
# creation de la fenêtre
class Window(QMainWindow): # création de la classe (fenêtre)
    def __init__(self):
        super(Window, self).__init__()
        
        self.tabs = QTabWidget() # création du Widget des onglets
        self.tabs.setDocumentMode(True) # supprime le cadre blanc autour des pages
        self.tabs.setTabsClosable(False) # autorise la fermeture des onglets
        self.setCentralWidget(self.tabs) # défini la barre d'onglet comme element central de la fenetre

        self.toolbar = QToolBar() # Création de la toolbar
        self.toolbar.setMovable(False) # empêche de pouvoir déplacer la toolbar
        self.toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon) # met le texte a côté du l'icone qui lui est associée
        self.toolbar.setFixedSize(500, 30) # défini la taille de la ToolBar
        self.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.toolbar) # ajout de la ToolBar sur la fenêtre et la place en pied de page

        # Création des QActions ("texte d'affichage") qui iront dans la QToolBar
        self.toolbar.addAction(QIcon('./utils/img/joystick.png'), 'Navigation')
        self.toolbar.addAction(QIcon('./utils/img/button_vert.png'), 'Intéragir')
        self.toolbar.addAction(QIcon('./utils/img/button_bleu.png'), 'Scanner QR-Code')
        self.toolbar.addAction(QIcon('./utils/img/button_rouge.png'), 'Retour')

        self.tabs.currentChanged.connect(self.update_current_browser) # met a jour la page lorsque qu'une nouvelle est ouverte (sert au fonctionnement du scroll)
        self.current_browser = self.tabs.currentWidget()
        self.cursor = self.cursor() # sauvegarde le curseur

        # affiche la page d'accueil comme page d'acceuil à l'ouverture de l'application
        self.add_new_tab(QUrl.fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+r'/web/html/index.html'))
        self.moveCursor(listeAccueil[j][0], listeAccueil[j][1])

        self.default_style_sheet() # appelle de la fonction qui s'occupe de la customisation de l'application
            



    #################################
    #### CREATIONS DES FONCTIONS ####
    #################################



    def open_scan(self):
        self.scanner = CameraApp() # créer une variable qui corresond à la caméra
        self.scanner.show() # affice le retour vidéo de la caméra
        self.scanner.start_camera(self.open_web_file) # lance la fonction qui gère la caméra


    # fonction permettant l'ajout de nouveaux onglets
    def add_new_tab(self, qurl=None, label='chargement...'):
        global j # importation de la variable j en tant que variable global

        if qurl is None: # on vérifie si l'url n'est pas vide
            qurl = QUrl('')

        browser = QWebEngineView() # creation de la partie graphique "moteur de rendu" qui affichera les fichiers ouverts
        # paramètrage afin de supporter les documents pdf
        browser.settings().setAttribute(browser.settings().WebAttribute.PluginsEnabled, True) # autorisarion des plugins dans le moteur de rendu
        browser.settings().setAttribute(browser.settings().WebAttribute.PdfViewerEnabled, True) # autorisation des fichiers pdf dans le moteur de rendu
        browser.setUrl(qurl) # ajoute la page avec l'url/fichier renseigner

        i = self.tabs.addTab(browser, label) # attribut l'onglet actuel à une variable
        self.tabs.setCurrentIndex(i) # fixe l'index de l'onglet
        
        # défini le titre de l'onglet et ouvre la page souhaiter dans le moteur de rendu
        browser.loadFinished.connect(lambda _, i=i, browser=browser: self.tabs.setTabText(i, browser.page().title()))
        j = 0 # réinitialise le compteur des boutons



    def open_web_file(self, data):
        global data_file # importation de la variable data_file en tant que variable global

        self.scanner.close()  # Fermer le scanneur de qrcode

        occurence = 0 # variable qui compte le nombre d'occurence de la data dans le nom des fichiers
        directory = os.path.split(os.path.abspath(__file__))[0]+r'/web/pdf' # dossier des pdf

        if (str(data) != '' and data is not None): # on verifie que la valeur du qrcode est différente de None et ' '
            for filename in os.listdir(directory): # on recupere tout les noms des fichiers du dossier renseigner ci-dessus

                if (filename == (str(data)+'.pdf') or (filename == (str(data)+'.mp4'))): # conditions qui permet de détecter si la data est comporté dans le nom d'un fichier
                    occurence += 1 # ajoute une occurence dès qu'un fichier comportant la data dans son nom est détécté

            if occurence == 0: # si le nombre d'occurence de la data est de 0
                print(f'Le fichier {str(data)}.pdf n\'existe pas !') # Le fichier n'a pas été trouvé, ce qui signifie qu'il n'existe pas 
                return
            elif occurence < 2: # si le nombre d'occurence de la data est inférieur à 2 donc égale à 1
                self.add_new_tab(QUrl.fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+rf'/web/pdf/{data}.pdf')) # on ajoute une nouvelle fenêtre comportant le fichier pdf que l'on souhaite ouvrir
                self.pdf_page_style_sheet() # on applique le style pour les pages pdf
            else:
                data_file = str(data) # on converti la data récupéra en chaîne de caractères
                self.add_new_tab(QUrl.fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+r'/web/html/selection.html')) # on ajoute une nouvelle fenêtre qui offre le choîx à l'utilisateur d'ouvrir soit un fichier pdf soit une vidéo
                self.moveCursor(listeSelection[j][0],listeSelection[j][1]) # on place le cursor sur le premier bouton de la page
                # ici le j est bien remis à 0 grace à la fonction add_new_tab

        else:
            # print('Le fichier est introuvable en raison de la data fournie qui est incorrect !')
            return


    def update_current_browser(self, i):
        # Actualise la valeur de self.current_browser quand l'onglet actif change
        self.current_browser = self.tabs.widget(i)


    # permet de fermer un onglet
    def close_current_tab(self):
        if self.tabs.count() < 2: # Garde au moins un onglet ouvert
            return # ne retourne rien pour faire aucune action et ne pas arreter le programme

        current_tab_index = self.tabs.currentIndex() # recupere l'index de l'onglet actuel
        self.tabs.removeTab(current_tab_index) # supprime l'onglet actuel
        self.default_style_sheet() # on applique la customisation par default de notre page


    ###################################
    ####  GESTION DES DEPLACEMENTS ####
    ###################################



    def moveCursor(self, x, y):
        self.cursor.setPos(x, y) # permet de choisir une positon précise pour le curseur sur la fenêtre


    def page_name(self):
        return str(self.current_browser.page().title()) # renvoie le titre de la page actuellement ouvert


    def moveLeft(self):
        global j # importation de la variable j en tant que variable global
        titre_page = self.page_name() # sauvegarde du nom de la page 

        self.current_browser.page().runJavaScript('window.scrollTo(0, window.scrollY -3000);') # on remonte la barre de scroll tout en haut pour bien voir ce que l'on fait
        
        if titre_page == 'Accueil': # si l'utilisateur ce situe sur la page d'acceuil
            liste = listeAccueil # coordonées accueil
            
            if j == 0: # si l'on ce situe sur le premier bouton
                j = 2 # on passe au dernier bouton
            else:
                j = j - 1 # sinon on passe au bouton précédent
        
        elif titre_page == 'Crédits' or titre_page == 'Séléction...': # si l'utilisateur ce situe sur la page des crédits ou la page de séléction
            if titre_page == 'Crédits':
                liste = listeCrédits # coordonées page crédits
            else:
                liste = listeSelection # coordonées page séléction
                
            
            if j == 0: # si l'on ce situe sur le premier bouton
                j = 1 # on passe au dernier bouton
            else:
                j = j - 1 # sinon on passe au bouton précédent
        else:
            return # ne pas deplacer horizontalement si ce n'est pas la page accueil ni crédits
        
        self.moveCursor(liste[j][0], liste[j][1])


    def moveRight(self):
        global j # importation de la variable j en tant que variable global
        titre_page = self.page_name() # sauvegarde du nom de la page 
        
        self.current_browser.page().runJavaScript('window.scrollTo(0, window.scrollY - 3000);') # on remonte la barre de scroll tout en haut pour bien voir ce que l'on fait
        
        if titre_page == 'Accueil':
            liste = listeAccueil # coordonées accueil
            
            if j == 2: # si l'on ce situe sur le dernier bouton
                j = 0 # on passe au permier bouton
            else:
                j = j + 1 # sinon on passe au bouton suivant
                
        elif titre_page == 'Crédits' or titre_page == 'Séléction...': # si l'utilisateur ce situe sur la page des crédits ou la page de séléction
            if titre_page == 'Crédits':
                liste = listeCrédits # coordonées page crédits
            else:
                liste = listeSelection # coordonées page séléction
            
            if j == 1:  # si l'on ce situe sur le dernier bouton
                j = 0 # on passe au permier bouton
            else:
                j = j + 1 # sinon on passe au bouton suivant
        else:
            return # ne pas deplacer horizontalement si ce n'est pas la page accueil ni crédits
        
        self.moveCursor(liste[j][0], liste[j][1]) # on place le curseur sur le premier bouton de la page
        
        
    def action_handler(self):
        global j, data_file # importation de la variable j en tant que variable global
        titre_page = self.page_name() # sauvegarde du nom de la page 
        
        if (j == 0 and titre_page == 'Accueil'):
            self.open_scan() #ouvre l'interface pour scanner un qrcode et recupere la valeur associé avec le qrcode
        
        # si l'on se situe sur la page acceuil et que l'on clique sur le bouton 2 alors on ouvre la page des crédits et on place le curseur sur le premier bouton de la page
        elif (j == 2 and titre_page == 'Accueil'):
            self.add_new_tab(QUrl.fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+r'/web/html/credits.html'))
            self.moveCursor(listeCrédits[j][0], listeCrédits[j][1])
        
        # si l'on se situe sur la page crédits et que l'on clique sur le bouton 0 alors on ouvre la page d'acceuil et on place le curseur sur le premier bouton de la page
        elif (j == 0 and titre_page == 'Crédits'):
            self.add_new_tab(QUrl.fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+r'/web/html/index.html'))
            self.moveCursor(listeAccueil[j][0], listeAccueil[j][1])
        
        # si l'on se situe sur la page de séléction de fichiers et que l'on clique sur le bouton 0 alors on ferme la page de séléction et on ouvre le fichier pdf dans le moteur de rendu puis on place le curseur sur le premier bouton de la page tout en appliquant le style pour les pages pdf
        elif (j == 0 and titre_page == 'Séléction...'):
            self.close_current_tab() # supprime l'onglet actif en recuperant son index
            self.add_new_tab(QUrl.fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+rf'/web/pdf/{data_file}.pdf'))
            self.moveCursor(listeAccueil[j][0],listeAccueil[j][1])
            self.pdf_page_style_sheet()
        
        # si l'on se situe sur la page de séléction de fichiers et que l'on clique sur le bouton 1 alors on ferme la page de séléction et on ouvre le fichier vidéo dans le moteur de rendu puis on place le curseur sur le premier bouton de la page tout en appliquant le style pour les pages vidéo
        elif (j == 1 and titre_page == 'Séléction...'):
            self.close_current_tab() # supprime l'onglet actif en recuperant son index
            self.add_new_tab(QUrl.fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+rf'/web/pdf/{data_file}.mp4'))
            self.moveCursor(listeAccueil[j][0],listeAccueil[j][1])
        
        # si rien ne correspond au cas énoncer ci-dessus, alors le programme passe la requête.
        else:
            return
        
    
    ################################
    #### GESTIONS DES COMMANDES ####
    ################################
        
    
    # Programmation Evénementielle
    # Fonctions qui détecte lorsque qu'une touche spécifique est pressée ou qu'une action précise est réalisée
    # Les actions proviennent du fichier command.py suite à l'activation d'un bouton ou du joystick
        
    def command_handler(self, command):
        if command == 'z':
            pyautogui.scroll(SCROLL_SPEED) # on monte la page vers le haut (scroll vers le haut)
        elif command == 's':
            pyautogui.scroll(-SCROLL_SPEED) # on descend la page (scroll versle bas)
        elif command == 'q':
            self.moveLeft() # déplace le curseur sur la gauche pour passer au bouton précédent
        elif command == 'd':
            self.moveRight() # déplace le curseur sur la droite pour passer au bouton suivant
        elif command == 'b':
            self.close_current_tab() # supprime l'onglet actif
        elif command == 'f':
            self.open_scan() # active la caméra
        elif command == 'x':
            self.action_handler() # ouvre le gestionnaire de commandes
        elif command == 'e':
            self.close() # ferme la fenetre actuel
            raise Exception('Vous venez de quittez l\'application.') # affiche un message d'arrêt et quitte l'application (en faisant crash)
            
            
            
    #####################################
    #### CUSTOMISATION DE LA FENETRE ####
    #####################################

    
    # style CSS sur l'application pour les pages pdf
    def default_style_sheet(self):
        self.setStyleSheet('''
            QWidget{
                background-color: rgb(24,24,24);
                border-color: transparent;
                color: #f2f2f9;
            }
            QTabBar::tab{
                background: black;
                border: 2px solid black;
                border-bottom-color: rgb(160,160,160);
                border-bottom-width: 1.3px;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
                padding: 5px 10px 5px 10px;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                border-color: rgb(160,160,160);
                border-width: 1.5px;
                border-bottom-color: black;
            }
            QTabBar::tab:!selected {
                margin-top: 2px;
                border-left-style: none;
                border-right-style: none;
            }
            QToolButton{
                background: transparent;
                padding: 5px;
                margin-top: 2px
                margin-right: 2px;
            }
                            ''')


    # style CSS sur l'application pour les pages vidéo
    def pdf_page_style_sheet(self):
        self.setStyleSheet('''
            QWidget{
                background-color: rgb(24,24,24);
                border-color: transparent;
                color: #f2f2f9;
            }
            QTabBar::tab{
                background: black;
                border: 2px solid black;
                border-bottom-color: rgb(160,160,160);
                border-bottom-width: 1.3px;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
                padding: 5px 10px 5px 10px;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background: rgb(50,54,57);
                border-color: rgb(160,160,160);
                border-width: 1.5px;
                border-bottom-color: rgb(50,54,57);
            }
            QTabBar::tab:!selected {
                margin-top: 2px;
                border-left-style: none;
                border-right-style: none;
            }
            QToolButton{
                background: transparent;
                padding: 5px;
                margin-top: 2px
                margin-right: 2px;
            }
                    ''')
    
