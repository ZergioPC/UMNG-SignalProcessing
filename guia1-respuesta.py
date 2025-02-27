"""
GUIA 1 -  PROCESAMIENTO DE SEÑALES
Sergio Palacios
"""
import numpy as np
import matplotlib.pyplot as plt

#Auxiliares
def graficar(titulo,xLabel,yLabel,color,xData,yData,descripcion,coord):
    plt.figure(num="Guia 1 - Sergio Palacios",facecolor=(color)) 
    plt.text(coord[0],coord[1],descripcion,ha='right',wrap=True,fontsize=10,backgroundcolor="#fff20030",color="#000000aa")
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

def ondaCuadrada(Fm,w,T,a=1,phi=0):
    s = []
    for t in range(Fm*T):
        aux = (np.sin((2*np.pi/Fm)*w*t))+phi
        if(aux < 0):
            s.append(-a)   
        else:
            s.append(a)
    return np.array(s)

# 1. señal sinusoidal de 1000Hz en 10 segs muestreo de 44100Hz, graficar 1 periodo

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
x1 = ondaSeno(muestreo,freq,tiempo)

graficar('Punto 1','tiempo(s)',r'señal $X_1$(t)','#c39cff',t[:periodo],x1[:periodo],txt,[0.01,0.40])

# 2. señal sinusoidal de 500Hz en 10 segs muestreo de 44100Hz, graficar 1 periodo

txt = ("""Generar una señal sinusoidal de 500Hz
       con una duración de 10 segs y una frecuencia
       de muestreo de 44100Hz, al momento de
       ejecutar graficar un periodo de esta señal."""
       )

freq = 500
tiempo = 10
muestreo = 44100

periodo = int(muestreo/freq)

t = np.linspace(0,10,muestreo)
x2 = ondaSeno(muestreo,freq,tiempo)

graficar('Punto 2','tiempo(s)',r'señal $X_2$(t)','#f5ca95',t[:periodo],x2[:periodo],txt,[0.02,0.40])

# 3. señal sinusoidal de 250Hz en 10 segs muestreo de 44100Hz, graficar 1 periodo

txt = ("""Generar una señal sinusoidal de 250Hz
       con una duración de 10 segs y una frecuencia
       de muestreo de 44100Hz, al momento de ejecutar
       graficar un periodo de esta señal"""
       )

freq = 250
tiempo = 10
muestreo = 44100

periodo = int(muestreo/freq)

t = np.linspace(0,10,muestreo)
x3 = ondaSeno(muestreo,freq,tiempo)

graficar('Punto 3','tiempo(s)',r'señal $X_3$(t)','#95daf5',t[:periodo],x3[:periodo],txt,[0.04,0.40])

# 4. Sumar 3 señales anteriores y graficar la señal resultante, graficar 1 periodo

txt = ("""Sumar las 3 señales generadas previamente
    y graficar la señal resultante, al momento de
    ejecutar graficar unicamente periodo 
    de esta señal."""
    )

periodo = int(periodo)+1
xSuma = np.array([(x1[i] + x2[i] + x3[i]) for i in range(44100)])

graficar('Punto 4','tiempo(s)',r'señal $X_{suma}$(t)','#9cf08b',t[:periodo],xSuma[:periodo],txt,[0.04,1])

# 5. señal cuadrada de 1000Hz en 10 segs muestreo de 44100Hz, graficar 1 periodo

txt = ("""Generar una señal cuadrada de 1000Hz
    con una duración de 10 segs y una frecuencia
    de muestreo de 44100Hz, al momento de ejecutar
    graficar un periodo de esta señal"""
    )

freq = 1000
tiempo = 10
muestreo = 44100

periodo = int(muestreo/freq)

t = np.linspace(0,10,muestreo)
s1 = ondaCuadrada(muestreo,freq,tiempo)

graficar('Punto 5','tiempo(s)',r'señal $S_1$(t)','#c39cff',t[:periodo],s1[:periodo],txt,[0.01,0.40])

# 6. señal cuadrada de 500Hz en 10 segs muestreo de 44100Hz, graficar 1 periodo

txt = ("""Generar una señal cuadrada de 500Hz
    con una duración de 10 segs y una frecuencia
    de muestreo de 44100Hz, al momento de ejecutar
    graficar un periodo de esta señal."""
    )

freq = 500
tiempo = 10
muestreo = 44100

periodo = int(muestreo/freq)

t = np.linspace(0,10,muestreo)
s2 = ondaCuadrada(muestreo,freq,tiempo)

graficar('Punto 6','tiempo(s)',r'señal $S_2$(t)','#f5ca95',t[:periodo],s2[:periodo],txt,[0.02,0.40])

# 7. señal cuadrada de 250Hz en 10 segs muestreo de 44100Hz, graficar 1 periodo

txt = ("""Generar una señal cuadrada de 250Hz
    con una duración de 10 segs y una frecuencia
    de muestreo de 44100Hz, al momento de ejecutar
    graficar unicamente un periodo de esta señal"""
    )

freq = 250
tiempo = 10
muestreo = 44100

periodo = int(muestreo/freq)

t = np.linspace(0,10,muestreo)
s3 = ondaCuadrada(muestreo,freq,tiempo)

graficar('Punto 7','tiempo(s)',r'señal $S_3$(t)','#95daf5',t[:periodo],s3[:periodo],txt,[0.04,0.40])

# 8. Sumar 3 señales anteriores y graficar la señal resultante, graficar 1 periodo

txt = ("""Sumar las 3 señales generadas previamente
    y graficar la señal resultante, al momento de
    ejecutar graficar unicamente periodo 
    de esta señal."""
    )

periodo = int(periodo)
sSuma = np.array([(s1[i] + s2[i] + s3[i]) for i in range(44100)])

graficar('Punto 8','tiempo(s)',r'señal $S_{suma}$(t)','#9cf08b',t[:periodo],sSuma[:periodo],txt,[0.04,1])