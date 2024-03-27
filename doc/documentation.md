# Documentation (pyqt6-pdf-qrocde)

Bienvenue sur la documentation du projet "pyqt6-pdf-qrcode", à l'intérieur de cette dernière vous retrouverez le fonctionnement du programme de façon détaillé de manière à pouvoir utiliser correctement le programme.  
> If you want there is an english version of this file: [*DOCUMENTATION* in english](./documentation_EN.md).

## Table des matières

 1. [Présentation](#presentation)
 2. [À savoir](#goodtoknow)
 3. [Installation](#installation)
 4. [Passer du joystick au clavier/souris](#switchjoytokey)
 5. [Créer un qrcode](#qrcode)
 6. [Où placer mes fichiers PDF ?](#pdf)
 7. [Utilisation et Navigation (joystick)](#usejoy)
 8. [Utilisation et Navigation (clavier/souris)](#usekey)
 9. [Problèmes connus](#knowissue)
 10. [Améliorations possibles](#improvements)
 11. [Réalisé avec](#madewith)
 12. [References](#ref)


<div id='presentation'/> 
  
## Présentation

Ce projet a été réalisé par des élèves de Terminale durant les heures consacrées à l'enseignement de la spécialité numérique et sciences informatiques (NSI), il constitue leur projet de l'année de Terminale.  

> Le projet participe au concours *[Les Throphées NSI](https://trophees-nsi.fr/)* qui récompense les meilleures créations des élèves participants.
  
*L'objectif de ce projet est de rendre la découverte des spécialités du bac aussi informatif que ludique au travers de l'utilisation d'un joystick, 4 boutons et d'une interface "moderne".  -Équipe de développement.*   
  
> Le projet a eu l'occasion d'être présenté lors des portes ouvertes du [Lycée Curie-Corot](https://curie-corot.lycee.ac-normandie.fr/).

<div id='goodtoknow'/> 

## À savoir

Ce projet a été conçu pour une utilisation sous `Ubuntu` sur `Raspberry Pi 4 8Gb` dans le but d'être intégré au sein d'une borne type "arcade".  
La navigation a été pensée pour se faire avec un joystick et 4 boutons, le tout connecté en USB à un microcontrôleur.

Le projet fonctionne également sur `Windows 10` et `Windows 11`.

**_Aucun autre système d'exploitation n'a été testé. Le comportement du programme pourrait se trouver altérer voir inutilisable dans certains cas de figure si vous utilisez un OS non testé !_**

<div id='installation'/> 

## Installation

L'installation du projet ce fait en deux partie:

- La Raspberry Pi-Pico (contient un mini-programme qui écrit une trame USB en boucle)
- L'application (ne se situe pas sur la raspberry pi-pico)

### Raspberry Pi-Pico:

> Cette partie est facultative si vous êtes [passer du joystick au clavier/souris](#switchjoytokey), si c'est le cas nous vous renvoyons à [l'installation de l'application](#installproject), sinon suivez les instructions ci-dessous !

Le fichier `main.py` contenu dans le [dossier pi-pico](../pi-pico) doit être téléchargé dans une raspberry pi-pico de sorte à ce que le fichier `main.py` ce lance au démarrage de cette dernière.

Ce mini-programme sert à écrire une trame USB pour le joystick et les boutons qui sera lu par le programme, il permet de connaître l'etat du joystick ou d'un bouton.

<div id='installproject'/>

### L'application:

> L'application quant à elle peut être placée n'importe où (tant que l'ensemble des fichiers reste groupés) hormis le même emplacement que celui où se situe le fichier `main.py` du [dossier pi-pico](../pi-pico) !

Pour installer le projet rendez-vous sur la [page d'accueil](https://github.com/SneaKxyz/pyqt6-pdf-qrcode/tree/main) et téléchargez le fichier ZIP de la dernière publication en date.  
Situés sur la partie gauche de l'écran vous devriez voir les dernières publications `(ex: v0.1.0-beta)`.

Une fois le fichier ZIP récupéré et extrait, il ne vous reste plus qu'à installer les modules nécessaires.  
Pour ce faire, la liste des modules requis par le programme est disponible dans le fichier [requirements.txt](../requirements.txt).

Pour installer les modules, il est **_recommandé d'utiliser_** : [PIP](https://github.com/pypa/pip) !

Avec pip:
```cmd
pip install [<module-name>]
```
```cmd
python -m pip install [<module-name>]
```
```cmd
python3 -m pip install [<module-name>]
```

Sur Linux sans pip:
```bash
sudo apt-get install python3-[<module-name>]
```

> *Libre à vous de choisir la façon dont vous installez vos modules.*

Une fois toutes ces étapes faites, il ne vous reste plus qu'à ouvrir les fichiers télécharger dans votre IDE préféré, de vous placer dans le fichier `main.py` et de démarrer le programme.

> Suggestions d'IDE : [Microsoft Visual Studio Code](https://code.visualstudio.com/), [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/), [Thonny](https://thonny.org/), etc...

<div id='switchjoytokey'/>

## Passer du joystick au clavier/souris

Si vous ne disposez pas de ces prérequis :
* 1 Joystick
* 4 Boutons
* 1 Microcontrôleur

Dirigez-vous dans le fichier `config.py` et remplacez :
```py
NAVIGATION_MODE='JOYSTICK' # change between 'JOYSTICK' or 'KEYBOARD_MOUSE'
```
 par 
 ```py
NAVIGATION_MODE='KEYBOARD_MOUSE' # change between 'JOYSTICK' or 'KEYBOARD_MOUSE'
```
Cela permettra d'utiliser le programme en version clavier/souris. Vous n'aurez donc pas besoin d'un microcontrôleur, de joystick ni même de boutons.

<div id='qrcode'/>

## Créer un qrcode

Pour créer un qrcode personnalisé, nous vous conseillons de vous rendre sur ce site : [QR Code Generator](https://fr.qr-code-generator.com/)

> Libre à vous de choisir un autre site de création de qrcode.

Une fois sur le site que vous avez choisi, renseigner la chaîne de caractères qui sera contenu dans le qrcode.  
`Attention votre chaîne de caractère doit respecter un certain format (ex pour le fichier cv_2024.pdf)`:

```py
"cv_2024.pdf" -> "cv_2024" # La chaîne de caractère doit être égale au nom du fichier pdf (vous ne devez pas renseigner l'extension de votre fichier).
```

Une fois votre qrcode prêt enregistrez-le, il permettra d'ouvrir votre fichier une fois scanner par la caméra.

<div id='pdf'/> 

## Où placer mes fichiers PDF ?

> Vous devez impérativement avoir créé un qrcode pour votre fichier PDF. Voir [Créer un qrcode](#qrcode)

Les fichiers PDF que vous souhaitez ouvrir doivent être placés dans un dossier spécifique [dossier des PDF](../sources/web/pdf) :

```py
"pyqt6-pdf-qrcode/sources/web/pdf/votre_fichier.pdf"
```

<div id='usejoy'/> 

## Utilisation et Navigation (joystick)

Version pour joystick et boutons :

 1. Utilisez le joystick pour naviguer à travers les menus affichés à l'écran en l'orientant vers le haut, le bas, la gauche et la droite.

 2. Pour scanner un QR code appuyez sur le **bouton bleu** ou sur **la page d'acceuil** appuyez sur " commencer " avec le bouton vert.

 3. Ensuite placez-vous dans le champ de vision de la caméra et scannez le QR code d'une spécialité avec notre lecteur intégré.

 > - Si vous souhaitez revenir sur la page précédente, appuyez sur le bouton rouge.  
 > - Appuyez sur le bouton noir pour fermer l'application.

<div id='usekey'/> 

## Utilisation et Navigation (clavier/souris)

> Comment utiliser mon clavier et ma souris plutôt qu'un joystick ? [Passer du joystick au clavier/souris](#switchjoytokey)

Voici la liste des contrôles au clavier et à la souris : 

* **'q'** ⇒ passer au bouton précédent
* **'d'** ⇒ passer au bouton suivant
* **'b'** ⇒ supprime l'onglet actif (retour arrière)
* **'f'** ⇒ active la caméra pour permettre de scanner un qrcode
* **'x'** ⇒ valider une action. Sur le bouton "commencer" cela lance la caméra.
* **'e'** ⇒ fermer l'application

> Utilisez la molette de votre souris pour défiler de haut en bas une page.

<div id='knowissue'/> 

## Problèmes connus

> Vous avez découvert un bug dans le programme ? N'hésitez pas à nous en faire part !

Voici une liste des problèmes connus :

* Sur Windows, il se peut qu'au démarrage une page blanche apparaisse, il vous suffit de monter et descendre la page pour actualiser.

* Il se peut que le défilement des boutons ne se passe pas correctement, essayez d'appuyer moins vite sur les touches de déplacement.

<div id='improvements'/> 

## Améliorations possibles

Ce projet possède plusieurs pistes d'amélioration, voici quelques-unes que nous avons imaginées:

> Vous avez une idée ? N'hésitez pas à nous le faire savoir !

* **Lecteur vidéo** : possibilité d'utiliser un lecteur vidéo, cependant quelques modifications sont à prévoir pour le rendre fonctionnel.
* **Liste fichiers récemment ouvert** : base de données qui stocke les noms des derniers fichiers ouverts et les affiches à l'utilisateur.
* **Site pour générer des qrcodes** : créer un site web pour a l'application pour générer des qrcodes, il pourra être ouvert localement puisque que l'app supporte les fichiers html.

<div id='madewith'/> 

## Réalisé avec

* [![Python][Python.org]][Python-url]
* [![Html][Html]][Html-url]
* [![Css][Css]][Css-url]
* [![Javascript][Javascript]][Javascript-url]

<div id='ref'/> 

## References

* [Les Throphées NSI](https://trophees-nsi.fr/)
* [Lycée Curie-Corot](https://curie-corot.lycee.ac-normandie.fr/)
* [PIP](https://github.com/pypa/pip)
* [Microsoft Visual Studio Code](https://code.visualstudio.com/)
* [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/)
* [Thonny](https://thonny.org/)
* [QR Code Generator](https://fr.qr-code-generator.com/)

*******


<!-- MARKDOWN -->
[Python.org]: https://img.shields.io/badge/python-0769AD?style=for-the-badge&logo=python&logoColor=yellow
[Python-url]: https://www.python.org/
[Html]: https://img.shields.io/badge/html-DD0031?style=for-the-badge&logo=html5&logoColor=white
[Html-url]: https://developer.mozilla.org/fr/docs/Web/HTML
[Css]: https://img.shields.io/badge/css-4A4A55?style=for-the-badge&logo=css3&logoColor=blue
[Css-url]: https://developer.mozilla.org/fr/docs/Web/CSS
[Javascript]: https://img.shields.io/badge/javascript-black?style=for-the-badge&logo=javascript&logoColor=yellow
[Javascript-url]: https://developer.mozilla.org/fr/docs/Web/JavaScript


