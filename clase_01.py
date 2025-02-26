"""     SEÑALES BÁSICAS EN PYTHON 
Cada numero trabajado aqui son BITS

range(a,b,c)
a = start, b = end c = periodo

mplt.plot(X,Y) continuas
mplt.stem(X,Y) discretas

x = [i+2 for i in range(10) if i%2== 0]
    [haz esto for este rango si esto se cumple]

"""
# Librerías requerídas
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

##  SEÑALES BÁSICAS
#n = np.arange(-5,5)     # Crea un array desde -2 a 2
#u = np.heaviside(n,1)   # señal escalón unitario (array que irá en el eje X, valor cuando sea 0)
#u = np.where(n>0,n,2)   # señal rampa (condicion ,  se cumple, no se cumple)    
#u = np.zeros_like(n); u[n==0] = 1   # señal delta o unitaria (array de ceros de n tamaño); 
#plt.stem(n,u)

## SIMULACIÓN DE SEÑALES SIMPLES

def ondaSeno(Fm,w,T,a=1,phi=0):
    s = []
    for t in range(Fm*T):
        s.append((a*np.sin((2*np.pi/Fm)*w*t))+phi)   #se convierte en radianes
    return np.array(s,dtype=np.int16)

def ondaCuadrada(Fm,w,T,a=1,phi=0):
    s = []
    for t in range(Fm*T):
        if (a*np.sin((2*np.pi/Fm)*w*t)+phi < 0):
            s.append(-1 * a)
        else:
            s.append(1 * a)
    return np.array(s,dtype=np.int16)

# Generar una señal de 3 segundos a 8khz de muestreo y 2hz de frecuencia

muestreo = 44100   
tiempo = 5
freq = 440

onda = ondaSeno(muestreo,freq,tiempo)
#onda = ondaCuadrada(muestreo,freq,tiempo)

plt.plot([i for i in range(len(onda))],onda*32767)
plt.show()

## CONVERSIÓN A .wav
# Usamos 16 bits

wavfile.write('./audios/clase_1-OndaCuadrada.wav',muestreo,onda)