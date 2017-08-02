import sys, time
import RPi.GPIO as GPIO

red_pin = 29
green_pin = 10
blue_pin = 31

GPIO.setwarnings(False)

def blink(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def turn_off(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def red_on():
    blink(red_pin)

def green_on():
    blink(green_pin)

def blue_on():
    blink(blue_pin)

def yellow_on():
    blink(red_pin)
    blink(green_pin)

def cyan_on():
    blink(green_pin)
    blink(blue_pin)

def magenta_on():
    blink(red_pin)
    blink(blue_pin)

def white_on():
    blink(red_pin)
    blink(green_pin)
    blink(blue_pin)

def red_off():
    turn_off(red_pin)

def green_off():
    turn_off(green_pin)

def blue_off():
    turn_off(blue_pin)
    

def yellow_off():
    turn_off(red_pin)
    turn_off(green_pin)

def cyan_off():
    turn_off(green_pin)
    turn_off(blue_pin)

def magenta_off():
    turn_off(red_pin)
    turn_off(blue_pin)

def white_off():
    turn_off(red_pin)
    turn_off(green_pin)
    turn_off(blue_pin)

def main():
    while True:
        cmd = input("Choose an option: ")
        if cmd == "red on":
            red_on()
        elif cmd == "red off":
            red_off()
        elif cmd == "green on":
            green_on()
        elif cmd == "green off":
            green_off()
        elif cmd == "blue on":
            blue_on()
        elif cmd == "blue off":
            blue_off()
        elif cmd == "yellow on":
            yellow_on()
        elif cmd == "yellow off":
            yellow_off()
        elif cmd == "cyan on":
            cyan_on()
        elif cmd == "cyan off":
            cyan_off()
        elif cmd == "magenta on":
            magenta_on()
        elif cmd == "magenta off":
            magenta_off()
        elif cmd == "white on":
            white_on()
        elif cmd == "white off":
            white_off()
        else:
            print("Not a valid command.")
    return

main()
