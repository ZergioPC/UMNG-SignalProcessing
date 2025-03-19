"""     SEÑALES BÁSICAS EN PYTHON 
Cada numero trabajado aqui son BITS

range(a,b,c)
a = start, b = end c = periodo

mplt.plot(X,Y) continuas
mplt.stem(X,Y) discretas

x = [i+2 for i in range(10) if i%2== 0]
    [haz esto for este rango si esto se cumple]

x = [n if n != 4 else 1 for n in range(5)]
    [condicional for este rango]

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
    return np.array(s)

def ondaCuadrada(Fm,w,T,a=1,phi=0):
    s = []
    for t in range(Fm*T):
        if (a*np.sin((2*np.pi/Fm)*w*t)+phi < 0):
            s.append(-1 * a)
        else:
            s.append(1 * a)
    return np.array(s)

# Generar una señal de 3 segundos a 8khz de muestreo y 2hz de frecuencia

muestreo = 44100   
duracion = 5
freq = 440.0
amplitud = 0.5

#onda = ondaSeno(muestreo,freq,duracion,a=amplitud)
onda = ondaCuadrada(muestreo,freq,duracion,a=amplitud)

tiempo = np.linspace(0,duracion,int(muestreo*duracion),endpoint=False)

#plt.plot(tiempo,onda)
#plt.show()

## CONVERSIÓN A .wav en 16 bits

onda_16bits = (onda*32767).astype(np.int16)
wavfile.write('./audios/clase_1-OndaCuadrada.wav',muestreo,onda_16bits)