# Horizons Crux Badges

![image](https://cdn.hackclub.com/019f9d0b-af3d-7e0b-ad1c-14d1e6c94284/1000002511%201.png)

E-ink badges for Horizons Crux! Made in Kicad. They use 2.66" E-ink screens with an RP2040 mcu. And they are made in the shape of a mantaray :D

Features: 

## Schematic

![image](https://cdn.hackclub.com/01a021b3-5ee6-7313-8f04-26008c431219/Screenshot%202026-08-21%20at%2010.22.52%E2%80%AFam.png)

Here is the schematic for this board. It is a normal rp2040 microcontroller with an E-ink driver integrated into it. 


## PCB

![image](https://cdn.hackclub.com/01a02edc-6a6e-725d-a43d-91a9873c54db/Screenshot%202026-08-23%20at%2011.42.57%E2%80%AFpm.png)

Here is the pcb layout and design. This is a 2 layer board that has a ground pour, as well as a 3v3 pour on the top side over where the mcu electronics are. 

The files for the individual art sections can be found labelled in the [/art](/art) directory.


### Art

![fkdsjflkd](art/back.png)

The art was drawn by [@variidian](https://github.com/variidian). The original art files and the vectorised sections for pcb production can be found in the [/art](/art) folder. 

## Firmware

The badge can be flashed using the [Badge Paint Website](https://badge-paint.notaroomba.dev/).

You draw what you want or load in the preset and fill in the details. you then need to flash a micropython .uf2 and it will then allow you to flash the badge.

This site was made by [@notaroomba](https://github.com/notaroomba)

#### Credits

Credit to [@variidian](https://github.com/variidian) for making the art for the badge and credit to [@notaroomba](https://github.com/notaroomba) for writing the software.

Also a thank you to [JLCPCB](https://jlcpcb.com) for sponsoring the badges!
