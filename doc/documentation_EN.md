# Documentation (pyqt6-pdf-qrocde)

Welcome to the documentation for the "pyqt6-pdf-qrcode" project. In it you will find a detailed description of how the program works, so that you can use it correctly.  
> Une version française de la documentation existe: [*DOCUMENTATION* en français](./documentation.md).

## Table of contents

 1. [Presentation](#presentation)
 2. [Good to know](#goodtoknow)
 3. [Installation](#installation)
 4. [Switch from joystick to keyboard/mouse](#switchjoytokey)
 5. [Create un qrcode](#qrcode)
 6. [Where to put my PDF files ?](#pdf)
 7. [Use and Navigation (joystick)](#usejoy)
 8. [Use and Navigation (keyboard/mouse)](#usekey)
 9. [Known issues](#knowissue)
 10. [Possible improvements](#improvements)
 11. [Achieved with](#madewith)
 12. [References](#ref)


<div id='presentation'/> 
  
## Presentation

This project was created by Terminale (Year 12) students during the hours devoted to teaching the Digital and Computer Science (NSI) speciality, and is their project for the Terminale year.  

> The project is a Normandy winner in the “originality prize” category of the 2024 edition of the *[Les Throphées NSI](https://trophees-nsi.fr/)* competition, which rewards the best creations of participating students.
  
*The goal of this project is to make discovering the baccalaureate specialities as informative as it is fun by using a joystick, 4 buttons and a "modern" interface.  -Development team*   
  
> The project was presented at the [Lycée Curie-Corot](https://curie-corot.lycee.ac-normandie.fr/) open days.

<div id='goodtoknow'/> 

## Good to know

This project was designed for use under `Ubuntu` on `Raspberry Pi 4 8Gb` with the aim of being integrated into an arcade-type kiosk.  
Navigation has been designed to use a joystick and 4 buttons, all connected via USB to a microcontroller.

The project also runs on `Windows 10` and `Windows 11`.

**_No other operating system has been tested. The programme's behaviour could be altered or even rendered unusable in certain cases if you use an untested OS!_**

<div id='installation'/> 

## Installation

The project is installed in two parts:

- The Raspberry Pi-Pico (contains a mini-program that writes a USB frame in a loop)
- The application (not located on the raspberry pi-pico)

### Raspberry Pi-Pico:

> This part is optional if you have [switched from joystick to keyboard/mouse](#switchjoytokey), if so we refer you to the [application installation](#installproject), otherwise follow the instructions below !

The `main.py` file contained in the [pi-pico folder](../pi-pico) must be downloaded to a raspberry pi-pico so that the `main.py` file is launched when the raspberry pi-pico is started.

This mini-program is used to write a USB frame for the joystick and buttons that will be read by the program, it allows you to know the state of the joystick or a button.

### The application:

> As for the application, it can be placed anywhere (as long as all the files remain grouped together) apart from the same location as the `main.py` file in the [pi-pico folder](../pi-pico) !

To install the project go to the [home page](https://github.com/SneaKxyz/pyqt6-pdf-qrcode/tree/main) and download the ZIP file for the latest release.  
On the left-hand side of the screen you should see the latest releases (e.g. v0.1.0-beta).

Once the ZIP file has been retrieved and extracted, all that's left to do is install the necessary modules.  
To do this, the list of modules required by the programme is available in the file [requirements.txt](../requirements.txt).

To install the modules, it is **_recommended to use_** : [PIP](https://github.com/pypa/pip) !

With pip:
```cmd
pip install [<module-name>]
```
```cmd
python -m pip install [<module-name>]
```
```cmd
python3 -m pip install [<module-name>]
```

On Linux without pip:
```bash
sudo apt-get install python3-[<module-name>]
```

> *It's up to you how you install your modules.*

Once all these steps have been completed, all that's left to do is launch the download files by executing the `launcher.bat` file on Windows or `launcher.sh` on Linux.  

Alternatively, in your favorite IDE, go to the `main.py` file and start the program.  

> IDE suggestions : [Microsoft Visual Studio Code](https://code.visualstudio.com/), [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/), [Thonny](https://thonny.org/), etc...

<div id='switchjoytokey'/>

## Switch from joystick to keyboard/mouse

If you do not have these requirements :
* 1 Joystick
* 4 buttons
* 1 Microcontroller

Go to the `./sources/config.py` file and replace :
```py
NAVIGATION_MODE='JOYSTICK' # change between 'JOYSTICK' or 'KEYBOARD_MOUSE'
```
 by 
 ```py
NAVIGATION_MODE='KEYBOARD_MOUSE' # change between 'JOYSTICK' or 'KEYBOARD_MOUSE'
```
This will allow the program to be used as a keyboard/mouse version. So you won't need a microcontroller, joystick or even buttons.

<div id='qrcode'/>

## Create a qrcode

To create a custom qrcode, you can use the app's built-in qrcode generator by going to the “create” tab on the home page.  

Alternatively, we recommend you visit this site: [Qrcode Generator](https://sneakxyz.github.io/qrcode-generator-website/).  

> You are free to choose another qrcode creation site.

Once on the site you have chosen, enter the character string that will be contained in the qrcode.  
`Note that your character string does not respect the format and will be case sensitive (e.g. for the file cv_2024.pdf)`:

```py
"cv_2024.pdf" # The string must be equal to the name of the file (you do need to enter the file extension).
```

Once your qrcode is ready, save it so that your file can be opened once the qrcode has been scanned by the camera.

<div id='pdf'/> 

## Where to put my PDF files ?

> You must have created a qrcode for your PDF file. See [Create a qrcode](#qrcode)

The PDF files you want to open must be placed in a specific folder [PDF folder](../sources/content/pdf) :

```py
"./sources/content/pdf/your_file.pdf"
```

<div id='usejoy'/> 

## Use and Navigation (joystick)

Version for joystick and buttons :

 1. Use the joystick to navigate the on-screen menus by pointing up, down, left and right.

 2. To scan a QR code press the **blue button** or on the **home page** press " scan " with the green button.

 3. Then place yourself in the field of vision of the camera and scan the QR code of a speciality with our integrated reader.

 > - If you want to return to the previous page, press the red button.  
 > - Press the black button to close the application.

<div id='usekey'/> 

## Use and Navigation (keyboard/mouse)

> How can I use my keyboard and mouse instead of a joystick? [Switching from joystick to keyboard/mouse](#switchjoytokey)

Here is the list of keyboard and mouse controls: 

* **'b'** ⇒ delete the active tab (back)
* **'c'** ⇒ activate the camera to scan a qrcode
* **'w'** ⇒ close the application

> Use your mouse wheel to scroll up and down a page.  
> Click your mouse buttons to interact with the application.  

<div id='knowissue'/> 

## Known issues

> Have you discovered a bug in the program? Don't hesitate to let us know!

Here's a list of known problems:

* ~~On Windows, a blank page may appear at start-up. Simply scroll up and down the page to refresh.~~  

* If the buttons don't scroll properly, try pressing the arrow keys more slowly.

* The camera may think it recognizes a qrcode, but stop because it can't retrieve any data.

<div id='improvements'/> 

## Possible improvements

There are a number of ways in which this project could be improved, and here are just a few of them:

> Do you have an idea? Don't hesitate to let us know!

* ~~**Video player**: a video player can be used, but a few changes are needed to make it work.~~
* ~~**Site to generate qrcodes**: create a website for the application to generate qrcodes, which can be opened locally as the application supports html files.~~
* ~~**Logs system**: save every error and can restart the application.~~
* **Recently opened files list**: database that stores the names of the most recently opened files and displays them to the user.
* **Startup/admin menu**: a menu that can be used as a pre-home to add files or other prerequisites to the program.
* **Integrated log console**: a program-integrated log console that appears when a certain action is performed, to display logs without leaving the application.

<div id='madewith'/> 

## Achieved with

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

> QR Code is a registered trademark of DENSO WAVE INCORPORATED

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


