import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)

p = GPIO.PWM(20, 1000)
p.start(0)
print('Введите s, чтобы остановить ')
p.stop()

try:
    while True:
        d = input('Введите значение duty cycle или q, чтобы выйти: ')
        if d == 'q':
            print('Выход')
            break
        p.start(int(d))
        #input('Введите s, чтобы остановить ')
        #p.stop()
        voltage = 3.3*int(d)/100
        print('Значение напряжения на ЦАП приблизительно равно ', voltage, ' B')
finally:
    GPIO.cleanup()