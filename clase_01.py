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

n = np.arange(-5,5)     # Crea un array desde -2 a 2

#u = np.heaviside(n,1)   # señal escalón unitario (array que irá en el eje X, valor cuando sea 0)
#u = np.where(n>0,n,2)   # señal rampa (condicion ,  se cumple, no se cumple)    
u = np.zeros_like(n); u[n==0] = 1   # señal delta o unitaria (array de ceros de n tamaño); 


amplitud = 1.0
freqM = 44100          #Frequencia de muestreo (cada cuanto toma muestra)

plt.stem(n,u)
plt.show()