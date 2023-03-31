import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0, 0, 0, 0, 0, 0, 0, 0]

GPIO.setup(dac, GPIO.OUT)
number = [0, 0, 0, 0, 0, 0, 0, 0]
GPIO.output(dac, number)
time.sleep(20)

GPIO.cleanup()      