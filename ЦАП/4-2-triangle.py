def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def is_num(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
    
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
x = input('Введите период: ')
if is_num(x) == True:
    t = float(x)
else:
    print("Неправильное число")
    exit
try:
    while True:
        for i in range(0, 256):
            binary = decimal2binary(i)
            for j in range(8):
                GPIO.output(dac[j], binary[j])
            time.sleep(t/(2*256))
        for i in range(256, 0, -1):
            binary = decimal2binary(i)
            for j in range(8):
                GPIO.output(dac[j], binary[j])
            time.sleep(t/(2*256))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()