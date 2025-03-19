""" CONVOLUCIONES CON SEÑALES EN PYTHON

!!importante: 
    x[n] = [1,2,3]
    x[-n] = [3,2,1]

1. 

"""
import numpy as np

def normalizar(lista):
    max = 0
    for n in lista:
        if ( np.abs(n) > max):
            max = n
    return [(n/max) for n in lista]

def convolucion(xn,hn):
    x = normalizar(xn)
    h = normalizar(hn[::-1])

    y = []

    #Convolución cuando T >= 0
    for n in range(len(h)-1):
        xAux = x[:(n+1)]    
        hAux = h[-(n+1):]  
        yAux = []           # Lista de resultado de multiplicaciones
        Aux = 0             # Sumatoria de multiplicaciones
        for i in range(len(xAux)):
            yAux.append(xAux[i]*hAux[i])
        for i in yAux:
            Aux += i
        y.append(Aux)
    
    #Convolución intermedia
    for n in range(len(x)-len(h)):
        xAux = x[n:len(h)+n]
        yAux = []               # Lista de resultado de multiplicaciones
        Aux = 0                 # Sumatoria de multiplicaciones
        for i in range(len(xAux)):
            yAux.append(xAux[i]*h[i])
        for i in yAux:
           Aux += i
        y.append(Aux)

    #Convolución cuando len(h)+T > len(x[n+T])
    for n in np.linspace(len(h)-1,0,len(h)):
        xAux = x[-(int(n)+1):]    
        hAux = h[:(int(n)+1)]  
        yAux = []           # Lista de resultado de multiplicaciones
        Aux = 0             # Sumatoria de multiplicaciones
        for i in range(len(xAux)):
            yAux.append(xAux[i]*hAux[i])
        for i in yAux:
            Aux += i
        y.append(Aux)
    
    print(y)

a = [1,0,2,0,1,0,3,0,4,0,1,2,3,4,0]
b = [3,4,-1,0,1]

convolucion(a,b)