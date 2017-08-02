from gpiozero import LED, Button
from time import sleep
from random import uniform
from sys import exit

left_name = input("left player name is ")
right_name = input("right player name is ")

right_button_wins = 0
left_button_wins = 0

led = LED(4)
right_button = Button(14)
left_button = Button(15)

user_input = input("Play? ")

def pressed(button):
        global user_input
        if button.pin.number == 14:
            global left_button_wins
            left_button_wins += 1
            print(left_name, "won the game",
                  str(left_button_wins), "times!")
        else:
            global right_button_wins
            right_button_wins += 1
            print(right_name, "won the game",
                  str(right_button_wins), "times!")
        user_input = input("Play again? ")

while user_input == "yes":
    led.on()
    sleep(uniform(1, 3))
    led.off()

    right_button.when_pressed = pressed
    left_button.when_pressed = pressed

