# Borne informative de Présentation

Ce projet a été créer pour faciliter la présentation des spécialités du baccalauréat à l'aide de qr-code.

> If you want there is an english version of this file: [*README* in english](./README_EN.md) !

## À propos du Projet

Ce projet a été conçu pour un usage sous Ubuntu sur Raspberry Pi 4 8Gb dans le but d'être intégré au sein d'une borne type "arcade". La navigation a été pensée pour se faire avec un joystick et 4 boutons, le tout relié à un microcontroleur connecté en USB.

Si vous ne disposez pas de ces prérequis, dans `config.txt` changez :
```py
NAVIGATION_MODE='JOYSTICK'
```
 par 
 ```py
 NAVIGATION_MODE='KEYBOARD_MOUSE'
```

Pour toute information complémentaire, réferez-vous à la documentation du projet dans `doc/documentation.txt`

## Installation

Le fichier `requirements.txt` liste l'entièreté des modules python nécessaires.

Pour installer un module éxécutez une commande ci-dessous en fonction de votre environnement:

Pip:

```bat
python -m pip install [<module-name>]
```
```bat
python3 -m pip install [<module-name>]
```


Linux:

```bash
sudo apt-get install python3-[<module-name>]
```

## Réalisé avec

* [![Python][Python.org]][Python-url]
* [![Html][Html]][Html-url]
* [![Css][Css]][Css-url]
* [![Javascript][Javascript]][Javascript-url]

## Contribution

Ce projet a été réalisé par des élèves de Terminale durant les heures consacrées à l'enseignement de la spécialité « numérique et sciences informatiques » (NSI), il constitue leur projet de l'année de Terminale.

Le projet a eu l'occasion d'être présenté lors des portes ouvertes du Lycée Curie-Corot.


<!-- MARKDOWN -->
[Python.org]: https://img.shields.io/badge/python-0769AD?style=for-the-badge&logo=python&logoColor=yellow
[Python-url]: https://www.python.org/
[Html]: https://img.shields.io/badge/html-DD0031?style=for-the-badge&logo=html5&logoColor=white
[Html-url]: https://developer.mozilla.org/fr/docs/Web/HTML
[Css]: https://img.shields.io/badge/css-4A4A55?style=for-the-badge&logo=css3&logoColor=blue
[Css-url]: https://developer.mozilla.org/fr/docs/Web/CSS
[Javascript]: https://img.shields.io/badge/javascript-black?style=for-the-badge&logo=javascript&logoColor=yellow
[Javascript-url]: https://developer.mozilla.org/fr/docs/Web/JavaScript
