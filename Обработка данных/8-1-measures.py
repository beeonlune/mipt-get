import matplotlib.pyplot as mplot
import matplotlib as mplib
import numpy as npy


bits = 8
Vref = 3.3 #опорное напряжение
N_markers = 100


settings = npy.loadtxt( "settings.txt", dtype = float )
d_data = npy.loadtxt( "data.txt", dtype = int ) #digital data (0 - 255 v)

period = settings[0] #средняя частота дискретизации
quantization = settings[1] #шаг квантования АЦП
size = d_data.size #размер массива напряжений конденсатора
a_data = d_data / ( 2 ** bits ) * Vref #analog data (0 V - Vref V)
maxtime = period * d_data.size #конечное значение времени измерений
datatime = npy.linspace(0, maxtime , num = d_data.size) #генерация последовательности чисел с одинаковым шагом
chargetime = d_data.argmax() * period #время зарядки
unchargetime = max(datatime) - chargetime #время разрядки

print('quantization = {}'.format(quantization))
print('d_data = {}'.format(d_data))
print('a_data = {}'.format(a_data))
print('period = {}'.format(period))
print('maxtime = {}'.format(maxtime))
print('size = {}'.format(d_data.size))
print('datatime = {}'.format(datatime))
print('chargetime = {}'.format(chargetime))
print('unchargetime = {}'.format(unchargetime))


fig, ax = mplot.subplots(figsize = (16, 10), dpi = 200) 
ax.set_title("Процесс заряда и разряда конденсатора в RC-цепочке", wrap = True)
ax.set_xlabel("Время, с")
ax.set_ylabel("Напряжение, В")
ax.set_xlim(0, maxtime)
ax.set_ylim(0, max( a_data ) * 1.1)
ax.text(chargetime + maxtime / 15, 0.8 * max(a_data), f"Время заряда: {chargetime:.2f} с\n\nВремя разряда: {unchargetime:.2f} с", fontsize = 20, color = "green")
ax.minorticks_on()
ax.grid(True)
ax.grid(True, "minor", ls = ":")
markrate = int(size / N_markers)
ax.plot(datatime, a_data, marker = 'v', markersize = 5, markeredgecolor = "red", markevery = markrate, color = "blue", alpha = 1, linewidth = 0.2, linestyle = "--", label = "U = U(t)")
ax.legend()
fig.savefig("graph.png")
fig.savefig("graph.svg")
#mplot.show()