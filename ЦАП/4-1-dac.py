def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        x = input('Введите число от 0 до 255: ')
        if x == "q":
            exit()
        if is_int(x) == False:
            print("Ввод не целого числа")
            continue
        number = int(x)
        if number < 0:
            print("Ввод отрицательного числа")
            continue
        if number > 255:
            print("Ввод значения, превышающего возможности ЦАП")
            continue
        print(number)
        binar = decimal2binary(number)
        for j in range(len(dac)):
            GPIO.output(dac[j], binar[j])
        print("Напряжение на ЦАП: ", number*3.3/256)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
        