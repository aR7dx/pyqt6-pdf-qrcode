# Documentation (pyqt6-pdf-qrocde)

Bienvenue sur la documentation du projet "pyqt6-pdf-qrcode", à l'intérieur de cette dernière vous retrouverais l'ensemble des concepts, idées et fonctionnalités du programme de façon détaillé de manière à pouvoir vous les comprendres et vous les appropriez.  
> English version of the documentation can be found [here](./documentation_EN.md).

## Table des matières

 1. [Presentation](#presentation)
 2. [A savoir](#goodtoknow)
 3. [Installation](#installation)
 4. [Passer du joystick au clavier/souris](#switchjoytokey)
 5. [Utilisation](#use)
 6. [test](#installation)
 7. [Problèmes connues](#knowissue)


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

<div id='use'/> 

## Utilisation

...

<div id='knowissue'/> 

## Problèmes connues








