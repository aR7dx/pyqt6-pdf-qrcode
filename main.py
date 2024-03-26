'''
hardware platform: Pi Pico
Console arcade Usb
Joystick Grove connecte à connecteur A1
2 boutons Grove connecte à D16

Resultat:
Convertit les entrées analogiques A0 et A1 en informations logiques avant, arriere, gauche, droite et neutre
Affiche l'état des boutons

brochage
E/S Digitales
D16/D17
D18/D19
D20/D21
Entrees analogiques 16 bits
A0
A1
A2
'''

from machine import ADC, Pin # module machine : gestion broches (entrees/sorties)
from time import sleep # module time : gestion timer

# Declaration des broches
X=ADC(0) # Entree analogique A0
Y=ADC(1) # Entree analogique A1

D16=Pin(16,Pin.IN) # declaration broche 16 en entree
D17=Pin(17,Pin.IN) # declaration broche 17 en entree
D18=Pin(18,Pin.IN) # declaration broche 18 en entree
D19=Pin(19,Pin.IN) # declaration broche 19 en entree

while True:
  #Entrees digitales
  ValueX = X.read_u16()
  ValueY = Y.read_u16()
  
  if ValueX > 50000 : # position du joystick sur l'axe des abscisses ( axe X )
    joystick='gauche'
  elif ValueX < 10000:
    joystick='droite' # position du joystick sur l'axe des abscisses ( axe X )
  elif ValueY > 50000 :
    joystick='haut' # position du joystick sur l'axe des ordonées ( axe Y )
  elif ValueY < 10000:
    joystick='bas' # position du joystick sur l'axe des ordonées ( axe Y )
  else:
    joystick='neutre' # position neutre ( ordonnée à l'origine )
    
  bpRouge = not(D16.value()) # Etat inverse boutons( renvoie True si actionné, False sinon)
  bpNoir = not(D17.value())
  bpVert = not(D18.value())
  bpBleu = not(D19.value())
  
  trame=','+ str(bpRouge) + ',' + str(bpNoir) + ',' + str(bpVert) + ',' + str(bpBleu) + ',' + joystick + ','
  print(trame.encode('utf-8')) # écrit 5 bytes
  
  sleep(0.1)