from gpiozero import PWMLED, Button, LED
from signal import pause
from time import sleep
import RPi.GPIO as GPIO
import random

R = PWMLED(5)
G = PWMLED(15)
B = PWMLED(6)

R_count = 0;
G_count = 0;
B_count = 0;

while True:
    if R_count != G_count:
        R.pulse()
        R_count = random.randint(0, 2)
    elif G_count != B_count:
        G.pulse()
        G_count = random.randint(0, 2)
    elif B_count != R_count:
        B.pulse()
        B_count = random.randint(0, 2)
    else:
        R_count = random.randint(0, 2)
        G_count = random.randint(0, 2)
        B_count = random.randint(0, 2)

    print(str(R_count), str(G_count), str(B_count))
    sleep(0.1)
