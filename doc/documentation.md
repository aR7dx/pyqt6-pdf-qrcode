# Documentation (pyqt6-pdf-qrocde)

Bienvenue sur la documentation du projet "pyqt6-pdf-qrcode", à l'intérieur de cette dernière vous retrouverez l'acheminement du programme de façon détaillé de manière à pouvoir utiliser correctement le programme.  
> If you want there is an english version of this file: [*DOCUMENTATION* in english](./documentation_EN.md).

## Table des matières

 1. [Presentation](#presentation)
 2. [A savoir](#goodtoknow)
 3. [Installation](#installation)
 4. [Passer du joystick au clavier/souris](#switchjoytokey)
 5. [Créer un qrcode](#qrcode)
 6. [Utilisation et Navigation (joystick)](#usejoy)
 7. [Utilisation et Navigation (keyboard)](#usekey)
 8. [Problèmes connus](#knowissue)
 9. [Amélioration possible](#improvements)
 10. [Réalisé avec](#madewith)


<div id='presentation'/> 
  
## Presentation

Ce projet a été réalisé par des élèves de Terminale durant les heures consacrées à l'enseignement de la spécialité numérique et sciences informatiques (NSI), il constitue leur projet de l'année de Terminale.  

Ce projet participe au concours *[Les Throphées NSI](https://trophees-nsi.fr/)* qui récompense les meilleurs créations des élèves participants.  
  
  
>*L'objectif de ce projet est de rendre la découverte des spécialités du bac aussi informative que ludique au travers de l'utilisation d'un joystick, 4 boutons et d'une interface "moderne".  -Equipe de dévelopment.*  

  
Le projet a eu l'occasion d'être présenté lors des portes ouvertes du Lycée Curie-Corot.

<div id='goodtoknow'/> 

## A savoir

Ce projet a été conçu pour une utilisation sous `Ubuntu` sur `Raspberry Pi 4 8Gb` dans le but d'être intégré au sein d'une borne type "arcade".  
La navigation a été pensée pour se faire avec un joystick et 4 boutons, le tout connecté en USB à un microcontroleur.

Le projet fonctionne également sur `Windows 10` et `Windows 11`.

**_Aucun autre systeme d'exploitation n'a été testé. Le comportement du programme pourrait se trouver altérer voir inutilisable dans certain cas de figure si vous utilisez un OS non testé !_**

<div id='installation'/> 

## Installation

Pour installer le projet rendez-vous sur la [page d'accueil](https://github.com/SneaKxyz/pyqt6-pdf-qrcode/tree/main) et téléchargez le fichier ZIP de la derniere publication en date.  
Situés sur la partie gauche de l'écran vous devriez voir les dernières publications `(ex: v0.1.0-beta)`.

Une fois le fichier ZIP récupérer et extrait, il ne vous reste plus qu'à installer les modules nécessaires.  
Pour ce faire la liste des modules requis par le programme sont dispoibles dans le fichier [requirements.txt](../requirements.txt).

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

> *Libre à vous de choisir la façon dont vous intallez vos modules.*

Une fois toutes ces étapes faites, il ne vous reste plus qu'à ouvrir les fichiers télécharger dans votre IDE préféré, de vous placer dans le fichier `main.py` et de démarrer le programme.

> Suggestion d'IDE : [Microsoft Visual Studio Code](https://code.visualstudio.com/), [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/), [Thonny](https://thonny.org/), etc...

<div id='switchjoytokey'/>

## Passer du joystick au clavier/souris

Si vous ne disposez pas de ces prérequis :
* 1 Joystick
* 4 Boutons
* 1 Microcontroleur

Dirigez-vous dans le fichier `config.py` et remplacez :
```py
NAVIGATION_MODE='JOYSTICK' # change between 'JOYSTICK' or 'KEYBOARD_MOUSE'
```
 par 
 ```py
NAVIGATION_MODE='KEYBOARD_MOUSE' # change between 'JOYSTICK' or 'KEYBOARD_MOUSE'
```
Cela permettra d'utiliser le programme en version clavier/souris. Vous n'aurez donc pas besoin d'un microcontroleur, de joystick ni même de boutons.

<div id='qrcode'/>

## Créer un qrcode

....

<div id='usejoy'/> 

## Utilisation et Navigation (joystick)

Version pour joystick et boutons :

 1. Utilisez le joystick pour naviguer à travers les menus affichées à l'écran.

 2. Pour scanner un QR code appuyez sur le bouton bleu ou sur la page d'acceuil appuyez sur commencer avec le bouton vert.

 3. Ensuite placez-vous dans le champ de vision de la caméra et scannez le QR code d'une spécialité avec notre lecteur intégré pour obtenir des détails spécifiques.

<div id='usekey'/> 

## Utilisation et Navigation (keyboard)

> Comment utliser mon clavier et ma souris plutôt qu'un joystick ? [Passer du joystick au clavier/souris](#switchjoytokey)

* **'q'** ⇒ passer au bouton précédent
* **'d'** ⇒ passer au bouton suivant
* **'b'** ⇒ supprime l'onglet actif
* **'f'** ⇒ active la caméra pour permettre de scanner un qrcode
* **'x'** ⇒ valider une action. Sur le bouton "commencer" cela lance la caméra.
* **'e'** ⇒ fermer l'application

<div id='knowissue'/> 

## Problèmes connus

> Vous avez découvert un bug dans le programme ? N'hésitez pas à nous en faire part !

Voici une liste des problèmes connus :

* Sur Windows, il se peut qu'au demarrage une page blanche apparaisse, il vous suffit de monter et descendre la page pour actualiser.

* Il se peut que le défilement des boutons ne se passe pas correctment, essayez d'appuyer moins vite sur les touches de déplacement.

<div id='improvements'/> 

## Amélioration possible

Ce projet possède plusieurs pistes d'amélioration, voici quelques-unes que nous avons imaginés:

> Vous avez une idée ? N'hésitez pas à nous le faire savoir !

* **Lecteur vidéo** : possibilté d'utiliser un lecteur vidéo, cependant quelques modifications sont à prévoir pour le rendre fonctionnel.
* **Liste fichiers récemment ouvert** : base de données qui stocke le nom des derniers fichiers ouvert et l'affiche à l'utisateur 
* ...


<div id='madewith'/> 

## Réalisé avec

* [![Python][Python.org]][Python-url]
* [![Html][Html]][Html-url]
* [![Css][Css]][Css-url]
* [![Javascript][Javascript]][Javascript-url]

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


