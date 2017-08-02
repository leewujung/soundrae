import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

n = 10
sums = 1
for counter in range(1, n + 1):
    print("LED on")
    GPIO.output(18,GPIO.HIGH)
    time.sleep(sums)
    print("LED off")
    GPIO.output(18,GPIO.LOW)
    time.sleep(sums)

