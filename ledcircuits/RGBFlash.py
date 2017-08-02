import time, random
import RPi.GPIO as GPIO
import threading

R = 29
G = 10
B = 31

PINS = [R, G, B]


def main():
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(PINS, GPIO.OUT, initial = GPIO.LOW)
        print("\n Press ^C (control-C) to exit the program.\n")
        while True:
            select_and_set_next_pin()
            if all(GPIO.input(pin) == GPIO.LOW for pin in PINS):
                select_and_set_next_pin()
            time.sleep(0.75)
    except KeyboardInterrupt:
        pass
    finally:
            GPIO.cleanup()
                   
def select_and_set_next_pin():
    next_pin = PINS[random.randint(0,2)]
    GPIO.output(next_pin, not GPIO.input(next_pin))

if __name__ == "__main__":
    main()
    

