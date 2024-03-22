# Presentation Kiosk App

This project was created to make it easier to present the specialities of the baccalauréat using qr-codes.

> Il existe une version française de ce fichier: [*README* en français](./README.md) et [*DOCUMENTATION* en français](./doc/documentation.md) !

## About project

This project was designed for use under Ubuntu on a Raspberry Pi 4 8Gb, with the aim of being integrated into an arcade-style kiosk. Navigation has been designed to use a joystick and 4 buttons, all connected to a USB microcontroller.

The project also runs on Windows 10 and Windows 11.

It is essential to have:

- 1 Joystick
- 4 Buttons
- 1 Microcontroller

If you do not have these prerequisites, in `config.py` replace :
```py
NAVIGATION_MODE='JOYSTICK' # change between 'JOYSTICK' or 'KEYBOARD_MOUSE'
```
by
 ```py
 NAVIGATION_MODE='KEYBOARD_MOUSE' # change between 'JOYSTICK' or 'KEYBOARD_MOUSE'
```

This will allow the program to be used as a keyboard/mouse version. You won't need a microcontroller, joystick or buttons.

For further information, please refer to the project documentation in [*doc/documentation.md*](./doc/documentation.md).

## Installation

The `requirements.txt` file lists all the python modules required.

To install a module run one of the commands below depending on your environment:

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

## Created with

* [![Python][Python.org]][Python-url]
* [![Html][Html]][Html-url]
* [![Css][Css]][Css-url]
* [![Javascript][Javascript]][Javascript-url]

## Contribution

This project was carried out by students in Terminale (final year of secondary school) during the hours devoted to teaching the "digital and computer sciences" (NSI) speciality, and is their project for the Terminale year.

The project was presented at the Lycée Curie-Corot open days.


<!-- MARKDOWN -->
[Python.org]: https://img.shields.io/badge/python-0769AD?style=for-the-badge&logo=python&logoColor=yellow
[Python-url]: https://www.python.org/
[Html]: https://img.shields.io/badge/html-DD0031?style=for-the-badge&logo=html5&logoColor=white
[Html-url]: https://developer.mozilla.org/fr/docs/Web/HTML
[Css]: https://img.shields.io/badge/css-4A4A55?style=for-the-badge&logo=css3&logoColor=blue
[Css-url]: https://developer.mozilla.org/fr/docs/Web/CSS
[Javascript]: https://img.shields.io/badge/javascript-black?style=for-the-badge&logo=javascript&logoColor=yellow
[Javascript-url]: https://developer.mozilla.org/fr/docs/Web/JavaScript
