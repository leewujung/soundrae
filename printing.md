
# Printing in the raspberry pi

Created on July 7, 2017

## Objective 

My second task when I began working on this project with Wu-Jung Lee was:

2. Set up printer at APL to print the figures from task 1 (printer IP in the attached file, 
   Hulk is black and white and Procolor is color. Procolor may be harder to set up.)

This was one of the tasks I needed to complete by around July 5, 2017.

### Disclaimer

The main purpose of this file will be describe the process I went through in trying to complete
this task. I will be describing strategies or "solutions" which did not end up helping me 
complete this task. I will also describing problems I encountered in in the printing process.

#### What worked.

So there are two printers I have to set the raspberry pi (denoted RPi from now on) to:

1. The HP LaserJet P3015
2. The Ricoh C6502

I immediately downloaded the CUPS printing interface using the following command on the terminal,
with reference to the webpage I used to help me [download it](https://help.ubuntu.com/lts/serverguide/cups.html).

```
sudo apt install cups
```

Then a week later after much difficulty, I asked for IT help (which honestly, I should have done much sooner).

He found a very simple solution to the problem I was having for the past week: I was not connected to the network
of printers. All I had to do to establish a connection with the network from what I can recall is to simply
connect the raspberry pi to that network via ethernet cable.

From there we mainly worked from the foomatic database to connect to our printers.

Using the PIXEL gui, I navigated to the printer settings as shown here:

![Picture](screenshots/2017-08-02-142249_1824x984_scrot.png)

What should come up is the printer settings interface. The two printers I wanted to set up are shown here already connected. One note however is that for the Ricoh, I managed to fix the yellow warning sign by connecting to the correct IP address for the printer. I was still able to print through the Ricoh before the fix, but the IP I used was the printer's own server.

![Picture](screenshots/print1.png)

From there, making sure I was connected to the cups server that holds the network of printers I wish to connect to via the servers tab, I then choose to add a printer. What pops up is an interface that gives you choices on what sort of printer you wish to add.

![Picture](screenshots/2017-08-02-143648_1824x984_scrot.png)

Since I want to connect to two network printers, I chose the network printers tab, and a dropdown menu of different available local printers are shown. The HP LaserJet P3015 printer is available with the hostname "Hulk". 

![Picture](screenshots/2017-08-02-143655_1824x984_scrot.png)

![Picture](screenshots/2017-08-02-144841_1824x984_scrot.png)

![Picture](screenshots/2017-08-02-144919_1824x984_scrot.png)

