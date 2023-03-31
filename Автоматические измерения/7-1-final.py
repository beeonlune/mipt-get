import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

dac = [10, 9, 11, 5, 6, 13, 19, 26]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

dac.reverse()

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    for i in range(256):
        GPIO.output(dac, decimal2binary(i))
        time.sleep(0.001)
        comp_out = GPIO.input(comp)
        time.sleep(0.001)
        if comp_out == 0:
            GPIO.output(dac, 0)
            time.sleep(0.01)
            return i
    GPIO.output(dac, 0)
    time.sleep(0.01)
    return 256

def adc_new():
    dac_val = [0] * 8 
    for i in range(0, 8):
        dac_val[i] = 1
        GPIO.output(dac, dac_val)
        time.sleep(0.001)
        comp_out = GPIO.input(comp)
        if comp_out == 0:
            dac_val[i] = 0
    weight = 1 
    sum = 0
    for i in range(8):
        sum += weight * dac_val[7 - i]
        weight *= 2
    GPIO.output(dac, 0)
    return sum



try:
    voltages = []
    GPIO.output(troyka, GPIO.HIGH)
    time_start = time.time()
    
    while(adc_new() <= 245):
        val = adc_new()
        GPIO.output(leds, decimal2binary(val))
        voltages.append(val)
        time.sleep(0.001)
        print(val)
    
    GPIO.output(troyka, GPIO.LOW)
    
    while(adc_new() >= 256 * 0.02):
        val = adc_new()
        GPIO.output(leds, decimal2binary(val))
        voltages.append(val)
        time.sleep(0.001)
        print(val)
    
    time_finish = time.time()
    plt.plot(voltages)
    
    with  open("data.txt", 'w')  as  data:
        for i in range(len(voltages)):
             data.write(str(voltages[i]) + '\n')
    
    with  open("settings.txt", 'w')  as  settings:
        settings.write(str(time_finish - time_start) +'\n')
        settings.write(str((time_finish - time_start) / len(voltages))+'\n')
        settings.write(str(len(voltages) / (time_finish - time_start))+'\n')
        settings.write(str(3.3*0.02)+"-"+str(3.3*0.97)+'\n')
        settings.write(str(3.3/256)+'\n')
    
    plt.show()
    
    print("Время эксперимента = ", (time_finish - time_start) / len(voltages), '\n')
    print("Время периода = ", time_finish - time_start, '\n')
    print("Средняя частота дискретизации = ",  len(voltages) / (time_finish - time_start), '\n')
    print((3.3/256), '\n')

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()