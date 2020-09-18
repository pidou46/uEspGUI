# uEspGUI

This is an attempt to build a software based micropython GUI for ESP32 mcu.

Nowadays, everybody hold a smartphone with him everywhere.

My guess is that it is more powerfull to use this smartphone to interact with an mcu.

mcu's are often short in resources (RAM, ROM, MIPS, ect...) and build fancy GUI for this devices is a challenge for the developer and eat resources that will not be available any-more for the core application.

Wireless communication with mcu is whildly available today. Sometimes the wireless device is becoming the mcu in this case the solution become even more efficient on cost and power consumption point of view. ESP32 is a good example.

## Wireless communication
micropython-ESP32 is BLE and WIFI enabled

I would choose WIFI to begin



## GUI toolkit

I have choosed Kivy for the following reasons:
- python library
- cross platform: Linux, Windows, OS X, Android, iOS
- responsive (support python asyncio)

# Related projects:
https://github.com/tve/mqboard

https://github.com/kevinkk525/pysmartnode


## Project breakdown

### client:
#### data:
1 client = 1 mcu

data is shared by all sensors objects and the client object. This allow each sensor to update the list and client to read it. 
sensors=liste de sensor

#### methods:
init: herite de iot client

add sensor: importe dynamiquement le module associé

write: envoie les données au serveur, re-initialise data
convert data to string using json module


read: lit les données depuis le serveur





### sensor:
n * sensor par client

#### methodes:
 init: ID, pins, 
 
 capture: ajoute une ligne a data avec ID+horodatage+donnees



### driver:
fonctions minimale pour faire fonctionner le capteur et/ou actionneur.

