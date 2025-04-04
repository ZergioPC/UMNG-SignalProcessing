""" 
SERIES DE FOURIER

Toda función periódica es posible de representar mediante
una serie sinusoidal

"""

import numpy as np
import matplotlib.pyplot as plt

FM = 44100

def seriefourier(nota,T,amplitudes):
    global FM
    
    serie = []

    for t in range(FM*T):
        suma = 0
        for n in range(len(amplitudes)):
            suma += amplitudes[n]*np.sin(n*(2*np.pi/FM)*nota*t)
        serie.append(suma)

    maxValue = max(serie)
    return [x/maxValue for x in serie]


def almostTransformadaFourier(x:list) -> list:
    array = []
    counter = 0
    for a in range(5):
        r=0
        i=0
        if (a==0):
            r += (np.e**(2*np.pi/5))*x[counter]
        else:
            r += (np.e**(2*a*np.pi/5))*x[counter]
        
        i += np.sin(a)*x[counter]

        array.append(str(r) + f"_{i}i")
        counter += 1
    
    return(array)


x = [[1, -1],[1, -1],[1, -1],[1, -1],[1, -1]]
rrr = almostTransformadaFourier(x)
for i in rrr:
    print(i)
#test = seriefourier(440,2,[65,77,34,32,12,70])

#plt.stem(test)
#plt.show()

