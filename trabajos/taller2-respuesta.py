"""
TALLER PRÁCTICO #1 -  PROCESAMIENTO DE SEÑALES
Sergio Palacios
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# AUXILIARES

def pendiente(x0,x1,y0,y1):
    return (y1-y0)/(x1-x0)

def recta(x0,y0,m):
    return y0-(m*x0)

def toDBFS(A):
    return 10*np.log10(A/32767)

def ondaSeno(Fm,w,T,a=1,phi=0):
    s = []
    for t in range(Fm*T):
        aux = (a*np.sin((2*np.pi/Fm)*w*t))+phi
        s.append(aux)   
    return np.array(s)

def ondaCuadrada(Fm,w,T,a=1,phi=0):
    s = []
    for t in range(Fm*T):
        aux = (np.sin((2*np.pi/Fm)*w*t))+phi
        if(aux < 0):
            s.append(-a)   
        else:
            s.append(a)
    return np.array(s)

def ondaTriangulo(Fm,w,T,a=1,phi=0):
    periodo = int(Fm/w)
    frecuencia = int(T*w)

    m1 = pendiente(0,periodo/4,0,1)
    b1 = recta(0,0,m1)
    m2 = pendiente(periodo/4,(3*periodo)/4,1,-1)
    b2 = recta(periodo/4,1,m2)
    m3 = pendiente((3*periodo)/4,periodo,-1,0)
    b3 = recta((3*periodo)/4,-1,m3)
    
    s = []

    for t in range(frecuencia):
        for x in range(periodo):
            if(x < periodo/4):
                s.append((m1*x)+b1)
            elif(x >= periodo/4 and x < 3*periodo/4):
                s.append((m2*x)+b2)
            else:
                s.append((m3*x)+b3)
    
    return np.array([i*a for i in s])

def ondaSierra(Fm,w,T,a=1,phi=0):
    periodo = int(Fm/w)
    frecuencia = int(T*w)

    m1 = pendiente(0,periodo/2,0,1)
    b1 = recta(0,0,m1)
    m2 = pendiente(periodo/2,periodo,-1,0)
    b2 = recta(periodo/2,-1,m2)
    
    s = []

    for t in range(frecuencia):
        for x in range(periodo):
            if(x <= periodo/2):
                s.append((m1*x)+b1)
            else:
                s.append((m2*x)+b2)
    
    return np.array([i*a for i in s])

class ejercicios:
    def __init__(self,onda1,freq1,onda2,freq2,amplitud,periodo):
        self.onda1 = onda1
        self.freq1 = freq1
        self.onda2 = onda2
        self.freq2 = freq2
        self.a = amplitud
        self.z = periodo/4
        self.w = periodo/8
        self.tiempo = 3
    
    def punto1(self):
        pass

onda = ondaSierra(8000,10,3,a=2)
tiempo = [t for t in range(len(onda))]

plt.plot(tiempo,onda)
plt.show()