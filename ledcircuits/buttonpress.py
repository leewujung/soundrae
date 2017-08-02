from gpiozero import Button
from time import sleep

clicks = 0
button = Button(14)
button1 = Button(15)

def number():
    global clicks
    clicks += 1
    print(clicks)

while True:
    if button.is_pressed:
        sleep(.1)
        number()
    elif button1.is_pressed:
        sleep(.1)
        print("pressed" + str(clicks) + " times")

pause()
