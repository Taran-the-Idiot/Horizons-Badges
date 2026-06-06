# Horizons crux badges



total time spent: 22 hours

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

Routed the rest of the e ink thingy. kinda feels messy but eh.

![image](https://cdn.hackclub.com/019e9c25-ebae-7187-ad6b-30921f91bea6/Screen%20Shot%202026-05-30%20at%202.10.17%20pm.png)

so the rese and res pins are actually different and I had them put down as the same on the schematic so I fixed that

![image](https://cdn.hackclub.com/019e9c27-1040-7427-883e-f197e8f296b2/Screen%20Shot%202026-05-30%20at%202.15.59%20pm.png)

I put the cap here

![image](https://cdn.hackclub.com/019e9c27-5bfd-7a04-b025-b8a63d212cd2/Screen%20Shot%202026-05-30%20at%202.24.58%20pm.png)

and routed with vias

![image](https://cdn.hackclub.com/019e9c27-99b3-762b-895d-fd699e11a9c7/Screen%20Shot%202026-05-30%20at%202.31.57%20pm.png)


I was also told that I did not need 3v3 traces that thick so i went and made thm all thin.

![image](https://cdn.hackclub.com/019e9c2a-0a47-7457-9339-a038461b3217/Screen%20Shot%202026-05-30%20at%202.43.06%20pm.png)


added a pour and thats the routing done

Time spent: 3 hours

## 31st of May


![image](https://cdn.hackclub.com/019e9c2a-a502-7829-9f62-51b00d73e9ea/Screen%20Shot%202026-05-31%20at%208.52.52%20pm.png)

I now have access to the art and shall begin tracing and porting everything over to kicad. since its a png and all on one layer, I need to separate it and turn it into an svg

This is like a really stupidly long process that includes putting down a bunch of spline points and adjusting the spline to fit all the curves and stuff



![image](https://cdn.hackclub.com/019e7daa-7c59-75b3-9573-2a29bc555f36/paste-1780224783719.png)

I did the cutlines, imported it into kicad and now it looks like this


![image](https://cdn.hackclub.com/019e9c2b-e314-7bd6-8c21-c5878abd3e88/Screen%20Shot%202026-05-31%20at%209.58.47%20pm.png)

I did the top mask layer

![image](https://cdn.hackclub.com/019e9c2d-fdf2-7aa1-a49e-9cafd06fad6d/Screen%20Shot%202026-05-31%20at%209.59.44%20pm.png)

Importing it in, it looks like this now. it was a bit difficult to line it up properly though

![image](https://cdn.hackclub.com/019e9c2e-88da-7e8d-ae34-61d4376656de/Screen%20Shot%202026-05-31%20at%2010.15.17%20pm.png)

starting top silkscreen and did one of the jellyfish. this is how many points there are. its actually such a pain. trick to doing this though is to just put a point at all the corners and points where the curve changes. and then use the line curve tool to make it match the curve its on. you could make a million points but imo this is quicker


![image](https://cdn.hackclub.com/019e9c30-b3c8-7ef6-9462-279afa464a34/Screen%20Shot%202026-05-31%20at%2010.32.13%20pm.png)


did the top thing 

gonna just image dump since its all pretty repetitive anyways

![image](https://cdn.hackclub.com/019e9c31-1588-7b5e-a187-ec1698bdc32d/Screen%20Shot%202026-05-31%20at%2010.51.15%20pm.png)

![image](https://cdn.hackclub.com/019e9c31-9476-7639-b426-c9bd072b1fe2/Screen%20Shot%202026-05-31%20at%2010.52.44%20pm.png)

![image](https://cdn.hackclub.com/019e9c31-b377-70d6-90f4-777213a7c967/Screen%20Shot%202026-05-31%20at%2011.15.44%20pm.png)



Done that layer. on to the next

I also added that dot at the top as a reference dot. since kicad imports all the layers and uses different centre points for each layer, I added the dot so i could export it with every layer and use it to line everything up.


![image](https://cdn.hackclub.com/019e9c33-0ae7-7343-b845-d186a14b7cfd/Screen%20Shot%202026-05-31%20at%2011.40.06%20pm.png)

Starting on the other layer, some of the stuff already matches so saves a bit of time for me, other stuff I need to still do/edit though



![image](https://cdn.hackclub.com/019e9c34-3920-79b0-86a5-7257f593ad2c/Screen%20Shot%202026-06-01%20at%209.26.20%20am.png)

yeah this side is going to be like 10x harder than the last one

I just put down all the points first and will now be smoothing this whole thing out

Time spent: 3.5 hours

## 1st-2nd of June

![image](https://cdn.hackclub.com/019e9c34-5536-7979-a9cd-93ce50f97408/Screen%20Shot%202026-06-02%20at%2011.14.36%20pm.png)

I spent these 2 days doing this and didnt really take any other ss because its all the same repetitive thing anyways

![image](https://cdn.hackclub.com/019e9c36-e227-7b46-9fc0-69c8f8125516/Screen%20Shot%202026-06-02%20at%2011.19.34%20pm.png)

mask layer ^^

![image](https://cdn.hackclub.com/019e9c37-1831-788b-9cd7-b34d122a84ae/Screen%20Shot%202026-06-02%20at%2011.19.42%20pm.png)

Silkscreen layer ^^^^^^

Time spent over those 2 days: 7 hours

## 3rd of June

![image](https://cdn.hackclub.com/019e9c37-6c00-7451-970d-7aac1aae46a7/Screen%20Shot%202026-06-03%20at%203.38.49%20pm.png)

Imported the layers into kicad and noticed some errors so i fixed them up manually. it was only like a 0.05mm gap but eh. helps sooth my ocd

![image](https://cdn.hackclub.com/019e9c39-1f1a-721e-8cc1-68a6dc949481/Screen%20Shot%202026-06-03%20at%204.02.54%20pm.png)

this is the final badge design!

(low quality image because this is the plugged into jlc version that shows the mask properly since kicad doesnt delete any silkscreen with bare copper underneath it.)

after that just finished the bom and got the jlc price

Time spent: 1.5 hours


## 5th of June

I went and got a design review from cyao, he gave me a whole essay of stuff to fix


![image](https://cdn.hackclub.com/019e9c3a-643c-74d0-85fd-9ef6736766d8/Screen%20Shot%202026-06-05%20at%2010.31.30%20pm.png)


changed these to 90. my references were wrong

![image](https://cdn.hackclub.com/019e9c60-07be-78ce-816d-2d146acbb0a9/Screen%20Shot%202026-06-05%20at%2010.31.35%20pm.png)

Fixed this up because I missed some stuff plus had some wrong numbers or the datasheet was wrong or smth idk

![image](https://cdn.hackclub.com/019e9c60-c2ea-7fc1-8d93-9c3ef6bc0cd7/Screen%20Shot%202026-06-05%20at%2010.31.40%20pm.png)

changed the model of this to a cheaper one


![image](https://cdn.hackclub.com/019e9c61-261a-7ba8-9054-95fea3e370fa/Screen%20Shot%202026-06-05%20at%2011.17.14%20pm.png)


Swapped to a footprint with thermal relief vias

![image](https://cdn.hackclub.com/019e9c61-b75b-7091-b680-d3db1615b186/Screen%20Shot%202026-06-05%20at%2011.35.02%20pm.png)

was told to add more vias for ground near the port and also added an amogus

made some other smaller changes

Time Spent: 2 hours


## 6th of june

Made some more changes from the cyao feedback


![image](https://cdn.hackclub.com/019e9c62-69e1-7fa9-a1e5-58a50df05c46/Screen%20Shot%202026-06-06%20at%203.27.01%20pm.png)



![image](https://cdn.hackclub.com/019e9c62-856d-72b5-8c42-f0cecff2153c/Screen%20Shot%202026-06-06%20at%203.27.03%20pm.png)

added a power plane for 3v3. was have made it the entire top layer but i have a lot of exposed copper so it might be dangerous or easily short and it really isnt needed in the places where there isnt any electronics so I just put it there so its better

I had to fiddle a lot with all the traces and stuff and how to actually implement the pour. I did some research and ended up with this. There was also a lot of re-routing and stuff, I had to move around a bunch of the parts for the e ink thing to fit in the extra 3 capacitors and I also needed to move stuff around because of the pour change and ground all needing to be routed differently. 

![image](https://cdn.hackclub.com/019e9c82-856a-7b5c-b0a6-8e0c0430c165/Screen%20Shot%202026-06-06%20at%203.28.43%20pm.png)


I went and changed up the names for everything on my schematic to include lcsc part numbers and also to change the 0.1uf caps into 100nf caps since they always error out jlc

Need to get another review now

Time spent: 4 hours



