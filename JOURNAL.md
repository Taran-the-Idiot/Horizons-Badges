# Horizons crux badges

## 29th of May

Started work on the badges

![image](https://cdn.hackclub.com/019e9bcf-a85f-7721-9624-f9d22989cf3f/Screen%20Shot%202026-05-29%20at%209.36.03%20pm.png)

Basic rp2040 starting stuff. the text boxes are there because people say wah wah wah organise your schematics. so here I am organising my schematic for the first time ever.


![image](https://cdn.hackclub.com/019e9bd2-1c50-727d-82d4-14c818e4f501/Screen%20Shot%202026-05-29%20at%209.43.14%20pm.png)


usbc with the esd protection thingy and the ldo. made it the same as I did for the dev board

![image](https://cdn.hackclub.com/019e9bd4-eea7-78da-95cc-97292e192e3c/Screen%20Shot%202026-05-29%20at%209.43.21%20pm.png)

I did however change these resistor values after a discussion with kai and nimit where I found out that the value actually matters. 20k means that this device is the dominant one over the device its connected to, 5.1k means its the submission device that listens to what the other device tells it to do like a good boy(girl?, thing?, idk).

![image](https://cdn.hackclub.com/019e9bd6-b36d-7fb9-8040-1078d36bc09f/Screen%20Shot%202026-05-29%20at%209.45.50%20pm.png)

got this reference diagram out from the datasheet of the e ink that I plan to use




![image](https://cdn.hackclub.com/019e9bd8-7aa0-7feb-b8f1-095fa2b2b23c/Screen%20Shot%202026-05-29%20at%209.52.11%20pm.png)



Made the first bit and flipped it because my e ink footprint is flipped and otherwise it would be a bit trippy


![image](https://cdn.hackclub.com/019e9bd9-1179-72d9-9a52-a9672ca23086/Screen%20Shot%202026-05-29%20at%209.59.18%20pm.png)

Did the e ink fpc side of things.

![bleh](https://cdn.hackclub.com/019e9bd9-97fa-7f19-b484-cfc4f03c6f8f/Screen%20Shot%202026-05-29%20at%2010.13.19%20pm.png)


Added the tags to the microcontroller

![image](https://cdn.hackclub.com/019e9bda-1575-720c-ba59-299ccff78bca/Screen%20Shot%202026-05-29%20at%2010.13.23%20pm.png)


In the end this is what that circuit looks like


Time spent: 1 hour


## 30th of May

![image](https://cdn.hackclub.com/019e9bda-8f7e-7276-b3df-516daaf9513e/Screen%20Shot%202026-05-30%20at%2011.11.59%20am.png)

Found a inductor that works with the specs needed and is a good size

![image](https://cdn.hackclub.com/019e9be8-27bf-74f9-a73c-5ff8d8ed3990/Screen%20Shot%202026-05-30%20at%2011.22.54%20am.png)

got the art for it from shurui. this was just the preview but it works enough for me to get a start until she wakes up from eep and gets me the full file

![image](https://cdn.hackclub.com/019e9be9-58cf-71c7-ae0e-7d0e66a95ef0/Screen%20Shot%202026-05-30%20at%2012.48.29%20am.png)

First I dumped all the parts and kinda positioned them roughly where I wanted

![image](https://cdn.hackclub.com/019e9be9-d281-77f5-a449-ee05ee03ee87/Screen%20Shot%202026-05-30%20at%2011.35.25%20am.png)


I turned the screenshot of the preview into a reverse silkscreen footprint so I could have an outline on where to put stuff


![image](https://cdn.hackclub.com/019e9bf1-4bef-7af0-afa9-2db4fc9ec15d/Screen%20Shot%202026-05-30%20at%2011.40.33%20am.png)

im placing the usb at an angle on the bottom left so it can avoid the e ink and also avoid an overglade situation where the e ink was pressed against the usbc port and broke

![image](https://cdn.hackclub.com/019e9c01-7d4d-7cb8-81b4-1da391f23141/Screen%20Shot%202026-05-30%20at%2011.47.29%20am.png)

So the traces are like very scuffed because I have it at a 35 degree angle. ts is stupidly difficult to trace and manage too



![image](https://cdn.hackclub.com/019e9bea-e37e-70dd-9861-81453b19759b/Screen%20Shot%202026-05-30%20at%2012.10.43%20pm.png)


Screw it im just gonna move it here

its pretty close to the e ink but thats a problem for later me

(the silkscreen rectangle is an outline of the eink screen btw. I use it to get a scale of reference for stuff)

![image](https://cdn.hackclub.com/019e9c03-3d2a-72d0-b88b-b6af5b755b3c/Screen%20Shot%202026-05-30%20at%2012.13.13%20pm.png)

okay so when i made that last one, i used kicads image to footprint converter to give it a set height of 100mm but i forgot to account for the fact that there was a bunch of padding on either side so the actual workable area became smaller. so I cropped my ss to be nearly touching



![image](https://cdn.hackclub.com/019e9c0e-6a73-75f5-bac3-73cb83d731c7/Screen%20Shot%202026-05-30%20at%2012.30.56%20pm.png)

gave everything general positions

![image](https://cdn.hackclub.com/019e9c04-f298-7f49-85b9-a063fc83de3c/Screen%20Shot%202026-05-30%20at%2012.14.25%20pm.png)

I now have a ton more clearance and a ton more space between the usbc and the E ink



![image](https://cdn.hackclub.com/019e9c0c-ab7b-7721-927b-d75ad9704b05/Screen%20Shot%202026-05-30%20at%2012.27.45%20pm.png)

changed the resistance on the idicator led from 2.2 ohms to 2.2k ohms. I am no longer putting 2 amps of current through a led


![image](https://cdn.hackclub.com/019e9c0d-c2e2-7a5a-bcab-5bf16d18e29b/Screen%20Shot%202026-05-30%20at%201.04.09%20pm.png)

Positioned the parts for the e ink part and got them ready to route

![image](https://cdn.hackclub.com/019e9c0f-b148-72c5-98f4-399001e7d170/Screen%20Shot%202026-05-30%20at%201.06.41%20pm.png)

![image](https://cdn.hackclub.com/019e9c10-2bba-72f1-ba2b-204ef1ac7689/Screen%20Shot%202026-05-30%20at%201.13.12%20pm.png)

positioned the decoupling caps and resistors for the 2040


![image](https://cdn.hackclub.com/019e9c10-9243-7c6f-8302-8a6764a1eddb/Screen%20Shot%202026-05-30%20at%201.16.40%20pm.png)

And there are the rest of the caps and the crystal


![image](https://cdn.hackclub.com/019e9c10-f1d8-7d1d-80e1-1ba9074df2e9/Screen%20Shot%202026-05-30%20at%201.22.10%20pm.png)

I moved the whole 2040 up and under the screen becaude there is easier pin access to it that way and there is also easier positioning for the flash since needs to be under the 2040 or else it needs to cross the data lines


![image](https://cdn.hackclub.com/019e9c12-cd44-7dc2-aa9c-94c25f59dc7d/Screen%20Shot%202026-05-30%20at%201.41.02%20pm.png)


Routed the ldo, flash and decoupling caps





![image](https://cdn.hackclub.com/019e9c12-4220-7bf9-87a5-3605b2bb110d/Screen%20Shot%202026-05-30%20at%201.41.06%20pm.png)

And also did the usbc

![image](https://cdn.hackclub.com/019e9c13-d5a5-7385-a6f5-b2b3ab99f3dd/Screen%20Shot%202026-05-30%20at%202.00.45%20pm.png)

routed the data lines to the microcontroller. I had to use 2 vias and rmove the decoupling cap because they wouldnt all fit


![image](https://cdn.hackclub.com/019e9c25-26d5-7c0c-9f3a-3c652d6246a7/Screen%20Shot%202026-05-30%20at%202.11.48%20pm.png)






## 31st of May








![image](https://cdn.hackclub.com/019e7daa-7c59-75b3-9573-2a29bc555f36/paste-1780224783719.png)