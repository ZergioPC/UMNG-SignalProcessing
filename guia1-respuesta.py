"""
GUIA 1 -  PROCESAMIENTO DE SEÑALES
Sergio Palacios
"""
import numpy as np
import matplotlib.pyplot as plt

#Auxiliares
def graficar(titulo,xLabel,yLabel,color,xData,yData,descripcion,coord):
    plt.figure(facecolor=(color)) 
    plt.text(coord[0],coord[1],descripcion,ha='right',wrap=True,fontsize=10)
    plt.title(titulo)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.plot(xData,yData) 
    plt.show()

def ondaSeno(Fm,w,T,a=1,phi=0):
    s = []
    for t in range(Fm*T):
        aux = (a*np.sin((2*np.pi/Fm)*w*t))+phi
        s.append(aux)   
    return np.array(s)

# 1. señal sinusoidal 1000Hz 10 segs muestreo de 44100Hz, graficar 1 periodo

txt = ("""Generar una señal sinusoidal de 1000Hz
       con una duración de 10 segs y
       una frecuencia de muestreo de 44100Hz, al
       momento de ejecutar graficar un periodo
       de esta señal"""
       )

freq = 1000
tiempo = 10
muestreo = 44100

periodo = int(muestreo/freq)

t = np.linspace(0,10,muestreo)
x = ondaSeno(muestreo,freq,tiempo)

graficar('Punto 1','tiempo(s)','señal X(t)','#c39cff',t[:periodo],x[:periodo],txt,[0.01,0])