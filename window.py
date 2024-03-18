# importation des différents modules
import os
import pyautogui

# importation du module PyQt6
from PyQt6.QtWidgets import QMainWindow, QTabWidget, QToolBar
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtWebEngineWidgets import QWebEngineView
from scan_qrcode import CameraApp # fichier qui gère les qrcodes

pyautogui.PAUSE = 0
listeAccueil = [(330,900),(1540,100),(1750,100)] # coordonnées de la page d'accueil
listeCrédits = [(1540,100),(1750,100)] # coordonnées de la page des crédits
listeSelection = [(760,615),(1170,615)] # coordonnées de la page de séléction
j = 0 # compteur (sert pour savoir quel action effectuer)
data_file = None # donnée récupérée par la caméra



###############################
#### CREATION DE LA CLASSE ####
###############################



# creation de la fenêtre
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.tabs = QTabWidget() # création du Widget des onglets
        self.tabs.setDocumentMode(True) # supprime le cadre blanc autour des pages
        self.tabs.setTabsClosable(False) # autorise la fermeture des onglets
        self.setCentralWidget(self.tabs) # défini la barre d'onglet comme élément central de la fenêtre

        self.toolbar = QToolBar() # Création de la ToolBar
        self.toolbar.setMovable(False) # empêche de pouvoir déplacer la ToolBar
        self.toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon) # met le texte à côté de l'icône qui lui est associée
        self.toolbar.setFixedSize(500, 30) # défini la taille de la ToolBar
        self.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.toolbar) # ajout de la ToolBar sur la fenêtre et la place en pied de page

        # Création des QActions qui iront dans la QToolBar
        self.toolbar.addAction(QIcon('./utils/img/joystick.png'), 'Navigation')
        self.toolbar.addAction(QIcon('./utils/img/button_vert.png'), 'Intéragir')
        self.toolbar.addAction(QIcon('./utils/img/button_bleu.png'), 'Scanner QR-Code')
        self.toolbar.addAction(QIcon('./utils/img/button_rouge.png'), 'Retour')

        self.tabs.currentChanged.connect(self.update_current_browser) # met a jour la page lorsque qu'une nouvelle est ouverte (sert au fonctionnement du scroll)
        self.current_browser = self.tabs.currentWidget()
        self.cursor = self.cursor()

        # affiche la page d'accueil comme première page à l'ouverture de l'application
        self.add_new_tab(QUrl.fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+r'/web/html/index.html'))
        self.moveCursor(listeAccueil[j][0], listeAccueil[j][1])

        self.default_style_sheet() # on appelle la fonction qui s'occupe de la customisation de l'application



    #################################
    #### CREATIONS DES FONCTIONS ####
    #################################



    def open_scan(self):
        self.scanner = CameraApp() # créer une variable qui corresond à la caméra
        self.scanner.show() # affice le retour vidéo de la caméra
        self.scanner.start_camera(self.open_web_file)


    # fonction permettant l'ajout de nouveaux onglets
    def add_new_tab(self, qurl=None, label='chargement...'):
        global j

        if qurl is None:
            qurl = QUrl('')

        browser = QWebEngineView() # creation de la partie graphique "moteur de rendu" qui affichera les fichiers ouverts
        # paramètrage afin de supporter les documents pdf
        browser.settings().setAttribute(browser.settings().WebAttribute.PluginsEnabled, True)
        browser.settings().setAttribute(browser.settings().WebAttribute.PdfViewerEnabled, True)
        browser.setUrl(qurl) # ajoute la page avec l'url/fichier renseigner

        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)
        
        # défini le titre de l'onglet
        browser.loadFinished.connect(lambda _, i=i, browser=browser: self.tabs.setTabText(i, browser.page().title()))
        j = 0



    def open_web_file(self, data):
        global data_file

        self.scanner.close()  # Fermer le scanneur de qrcode

        occurence = 0 # nombre de fois qu'apparaît la data dans le nom des fichiers
        directory = os.path.split(os.path.abspath(__file__))[0]+r'/web/pdf' # dossier des fichiers pdf

        if (str(data) != '' and data is not None): # on verifie que la valeur du qrcode est différente de None et ' '
            for filename in os.listdir(directory): # on recupere tout les noms des fichiers du dossier renseigner ci-dessus

                if (filename == (str(data)+'.pdf') or (filename == (str(data)+'.mp4'))):
                    occurence += 1

            if occurence == 0:
                print(f'Le fichier {str(data)}.pdf n\'existe pas !')
                return
            elif occurence < 2:
                self.add_new_tab(QUrl.fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+rf'/{data}.pdf'))
                self.pdf_page_style_sheet()
            else:
                data_file = str(data)
                self.add_new_tab(QUrl.fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+r'/web/html/selection.html'))
                self.moveCursor(listeSelection[j][0],listeSelection[j][1])
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
        self.cursor.setPos(x, y) # permet de déplacer la souris


    def page_name(self):
        return str(self.current_browser.page().title()) # renvoie le titre de la page actuellement ouvert


    def moveLeft(self):
        global j
        titre_page = self.page_name()

        self.current_browser.page().runJavaScript('window.scrollTo(0, window.scrollY -3000);') # on remonte la barre de scroll tout en haut pour bien voir ce que l'on fait
        
        if titre_page == 'Accueil':
            liste = listeAccueil # coordonées accueil
            
            if j == 0:
                j = 2
            else:
                j = j - 1
        
        elif titre_page == 'Crédits' or titre_page == 'Séléction...':
            if titre_page == 'Crédits':
                liste = listeCrédits # coordonées page crédits
            else:
                liste = listeSelection # coordonées page séléction
                
            
            if j == 0:
                j = 1
            else:
                j = j - 1
        else:
            return # ne pas deplacer horizontalement si ce n'est pas la page accueil ni crédits
        
        self.moveCursor(liste[j][0], liste[j][1])


    def moveRight(self):
        global j
        titre_page = self.page_name()
        
        self.current_browser.page().runJavaScript('window.scrollTo(0, window.scrollY - 3000);') # on remonte la barre de scroll tout en haut pour bien voir ce que l'on fait
        
        if titre_page == 'Accueil':
            liste = listeAccueil # coordonées accueil
            
            if j == 2:
                j = 0
            else:
                j = j + 1
                
        elif titre_page == 'Crédits' or titre_page == 'Séléction...':
            if titre_page == 'Crédits':
                liste = listeCrédits # coordonées page crédits
            else:
                liste = listeSelection # coordonées page séléction
            
            if j == 1:
                j = 0
            else:
                j = j + 1
        else:
            return # ne pas deplacer horizontalement si ce n'est pas la page accueil ni crédits
        
        self.moveCursor(liste[j][0], liste[j][1])
        
        
    def action_handler(self):
        global j, data_file
        titre_page = self.page_name()
        
        if (j == 0 and titre_page == 'Accueil'):
            self.open_scan() #ouvre l'interface pour scanner un qrcode et recupere la valeur associé avec le qrcode
        
        elif (j == 2 and titre_page == 'Accueil'):
            self.add_new_tab(QUrl.fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+r'/web/html/credits.html'))
            self.moveCursor(listeCrédits[j][0], listeCrédits[j][1])
        
        elif (j == 0 and titre_page == 'Crédits'):
            self.add_new_tab(QUrl.fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+r'/web/html/index.html'))
            self.moveCursor(listeAccueil[j][0], listeAccueil[j][1])
        
        elif (j == 0 and titre_page == 'Séléction...'):
            self.close_current_tab() # supprime l'onglet actif en recuperant son index
            self.add_new_tab(QUrl.fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+rf'/web/pdf/{data_file}.pdf'))
            self.moveCursor(listeAccueil[j][0],listeAccueil[j][1])
            self.pdf_page_style_sheet()
        
        elif (j == 1 and titre_page == 'Séléction...'):
            self.close_current_tab() # supprime l'onglet actif en recuperant son index
            self.add_new_tab(QUrl.fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+rf'/web/pdf/{data_file}.mp4'))
            self.moveCursor(listeAccueil[j][0],listeAccueil[j][1])
        
        else:
            return
        
    
    ################################
    #### GESTIONS DES COMMANDES ####
    ################################
        
       
    # Fonctions qui détecte lorsque qu'une touche spécifique est pressée ou qu'une action précise est réalisée   
        
    def command_handler(self, command):
        if command == 'z':
            pyautogui.scroll(1) # on remonte la barre de scroll
        elif command == 's':
            pyautogui.scroll(-1) # on descend la barre de scroll
        elif command == 'q':
            self.moveLeft() # déplace le curseur à gauche
        elif command == 'd':
            self.moveRight() # déplace le curseur à droite
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
    
