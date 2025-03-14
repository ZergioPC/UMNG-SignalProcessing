"""
PROYECTO NÚMERO #1 -  PROCESAMIENTO DE SEÑALES
Sergio Palacios
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

#   FUNCIÓNES Y SETUP   #

notas_musicales = {
    "do":32.7,
    "do#":34.65,
    "re":36.71,
    "re#":38.89,
    "mi":41.2,
    "fa":43.65,
    "fa#":46.25,
    "sol":49.00,
    "sol#":51.91,
    "la":55.00,
    "la#":58.27,
    "si":61.74
}

def frecuenciaMusical(nota,octava):
    return (nota)*(2**(octava+1))

def tempo(bpm,n):
    if(n==0):
        tiempo = (4*(44100*60))/bpm
    elif(n==1):
        tiempo = (2*(44100*60))/bpm
    elif(n==2):
        tiempo = ((44100*60))/bpm
    elif(n==4):
        tiempo = (0.5*(44100*60))/bpm
    elif(n==8):
        tiempo = (0.25*(44100*60))/bpm
    
    return tiempo/44100.0

def ondaCuadrada(w,T,a,phi=0):
    Fm = 44100
    s = []
    for t in range(int(Fm*T)):
        aux = (np.sin((2*np.pi/Fm)*w*t))+phi
        if(aux < 0):
            s.append(-a)   
        else:
            s.append(a)
    return s

def ondaSeno(w,T,a,phi=0):
    Fm = 44100
    s = []
    for t in range(int(Fm*T)):
        aux = (a*np.sin((2*np.pi/Fm)*w*t))+phi
        s.append(aux)   
    return s

def ondaSierra(w,T,a):
    def pendiente(x0,x1,y0,y1):
        return (y1-y0)/(x1-x0)

    def recta(x0,y0,m):
        return y0-(m*x0)
    
    Fm = 44100
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
    
    return [i*a for i in s]

def ondaSilencio(w,T,a):
    return [0 for i in range(int(44100*T))]

def melody(array,nota,bpm,n,octava,onda,v=0.2):
    w = frecuenciaMusical(nota,octava)
    t = tempo(bpm,n)

    return np.concatenate((array,onda(w,t,a=v)))

def acorde(array,notas,bpm,n,octava,onda,v=0.7):
    w1 = frecuenciaMusical(notas[0],octava)
    w2 = frecuenciaMusical(notas[1],octava)
    w3 = frecuenciaMusical(notas[2],octava)
    t = tempo(bpm,n)

    first = np.array(onda(w1,t,a=v))
    third = np.array(onda(w2,t,a=v))
    five = np.array(onda(w3,t,a=v))

    onda = first+third+five

    return np.concatenate((array,onda))

"""
CANCIÓN: ASGORE (Undertale OST)
Autor: Toby Fox
"""
compaz = 115

#Parte 1
lead_parte1 = []
sublead_parte1 = []

def letmotive1(array,onda,octava=0):
    array = melody(array,notas_musicales["mi"],compaz,4,3+octava,onda)
    array = melody(array,notas_musicales["do"],compaz,4,0,ondaSilencio)
    array = melody(array,notas_musicales["sol#"],compaz,4,3+octava,onda)
    array = melody(array,notas_musicales["do"],compaz,4,0,ondaSilencio)

    array = melody(array,notas_musicales["fa#"],compaz,2,3+octava,onda)
    array = melody(array,notas_musicales["do"],compaz,4,0,ondaSilencio)
    array = melody(array,notas_musicales["sol#"],compaz,4,3+octava,onda)
    array = melody(array,notas_musicales["do#"],compaz,4,3+octava,onda)
    array = melody(array,notas_musicales["do#"],compaz,8,3+octava,onda)
    array = melody(array,notas_musicales["re#"],compaz,4,3+octava,onda)
    array = melody(array,notas_musicales["re#"],compaz,8,3+octava,onda)
    return array

ondaActual = ondaCuadrada
lead_parte1 = letmotive1(lead_parte1,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["mi"],compaz,4,3,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["sol#"],compaz,2,3,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["sol#"],compaz,4,3,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["do"],compaz,4,0,ondaSilencio)

lead_parte1 = letmotive1(lead_parte1,ondaActual)

lead_parte1 = melody(lead_parte1,notas_musicales["si"],compaz,4,3,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["sol#"],compaz,2,3,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["sol#"],compaz,4,3,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["do"],compaz,4,0,ondaSilencio)


lead_parte1 = melody(lead_parte1,notas_musicales["sol#"],compaz,4,3,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["do"],compaz,4,0,ondaSilencio)
lead_parte1 = melody(lead_parte1,notas_musicales["la"],compaz,4,3,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["do"],compaz,4,0,ondaSilencio)

lead_parte1 = melody(lead_parte1,notas_musicales["si"],compaz,2,3,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["do"],compaz,4,0,ondaSilencio)
lead_parte1 = melody(lead_parte1,notas_musicales["do#"],compaz,4,4,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["mi"],compaz,4,3,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["mi"],compaz,8,3,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["fa#"],compaz,4,3,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["fa#"],compaz,8,3,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["sol#"],compaz,4,3,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["si"],compaz,2,3,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["si"],compaz,4,3,ondaActual)

lead_parte1 = melody(lead_parte1,notas_musicales["do#"],compaz,4,4,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["re#"],compaz,4,3,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["re#"],compaz,8,3,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["re#"],compaz,4,4,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["re#"],compaz,8,4,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["si"],compaz,4,3,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["sol#"],compaz,1,3,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["sol#"],compaz,2,3,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["do"],compaz,4,2,ondaSilencio)

lead_parte1 = melody(lead_parte1,notas_musicales["la"],compaz,8,3,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["sol#"],compaz,8,3,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["fa#"],compaz,2,3,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["fa#"],compaz,4,3,ondaActual)
lead_parte1 = melody(lead_parte1,notas_musicales["do"],compaz,4,2,ondaSilencio)

ondaActual = ondaSilencio
sublead_parte1 = letmotive1(sublead_parte1,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["mi"],compaz,4,3,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["sol#"],compaz,2,3,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["sol#"],compaz,4,3,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["do"],compaz,4,0,ondaSilencio)

sublead_parte1 = letmotive1(sublead_parte1,ondaActual)

sublead_parte1 = melody(sublead_parte1,notas_musicales["si"],compaz,4,3,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["sol#"],compaz,2,3,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["sol#"],compaz,4,3,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["do"],compaz,4,0,ondaSilencio)

ondaActual = ondaSierra
sublead_parte1 = melody(sublead_parte1,notas_musicales["sol#"],compaz,4,3,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["do"],compaz,4,0,ondaSilencio)
sublead_parte1 = melody(sublead_parte1,notas_musicales["la"],compaz,4,3,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["do"],compaz,4,0,ondaSilencio)

sublead_parte1 = melody(sublead_parte1,notas_musicales["si"],compaz,2,3,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["do"],compaz,4,0,ondaSilencio)
sublead_parte1 = melody(sublead_parte1,notas_musicales["do#"],compaz,4,4,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["mi"],compaz,4,3,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["mi"],compaz,8,3,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["fa#"],compaz,4,3,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["fa#"],compaz,8,3,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["sol#"],compaz,4,3,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["si"],compaz,2,3,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["si"],compaz,4,3,ondaActual)

sublead_parte1 = melody(sublead_parte1,notas_musicales["do#"],compaz,4,4,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["re#"],compaz,4,3,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["re#"],compaz,8,3,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["re#"],compaz,4,4,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["re#"],compaz,8,4,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["si"],compaz,4,3,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["sol#"],compaz,1,3,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["sol#"],compaz,2,3,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["do"],compaz,4,2,ondaSilencio)

sublead_parte1 = melody(sublead_parte1,notas_musicales["la"],compaz,8,3,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["sol#"],compaz,8,3,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["fa#"],compaz,2,3,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["fa#"],compaz,4,3,ondaActual)
sublead_parte1 = melody(sublead_parte1,notas_musicales["do"],compaz,4,2,ondaSilencio)

## octava mas abajo
lead2_parte1 = []
ondaActual = ondaCuadrada
lead2_parte1 = letmotive1(lead2_parte1,ondaActual,octava=-1)
lead2_parte1 = melody(lead2_parte1,notas_musicales["mi"],compaz,4,2,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["sol#"],compaz,2,2,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["sol#"],compaz,4,2,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["do"],compaz,4,0,ondaSilencio)

lead2_parte1 = letmotive1(lead2_parte1,ondaActual,octava=-1)

lead2_parte1 = melody(lead2_parte1,notas_musicales["si"],compaz,4,2,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["sol#"],compaz,2,2,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["sol#"],compaz,4,2,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["do"],compaz,4,0,ondaSilencio)


lead2_parte1 = melody(lead2_parte1,notas_musicales["sol#"],compaz,4,2,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["do"],compaz,4,0,ondaSilencio)
lead2_parte1 = melody(lead2_parte1,notas_musicales["la"],compaz,4,2,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["do"],compaz,4,0,ondaSilencio)

lead2_parte1 = melody(lead2_parte1,notas_musicales["si"],compaz,2,2,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["do"],compaz,4,0,ondaSilencio)
lead2_parte1 = melody(lead2_parte1,notas_musicales["do#"],compaz,4,3,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["mi"],compaz,4,2,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["mi"],compaz,8,2,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["fa#"],compaz,4,2,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["fa#"],compaz,8,2,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["sol#"],compaz,4,2,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["si"],compaz,2,2,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["si"],compaz,4,2,ondaActual)

lead2_parte1 = melody(lead2_parte1,notas_musicales["do#"],compaz,4,3,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["re#"],compaz,4,2,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["re#"],compaz,8,2,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["re#"],compaz,4,3,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["re#"],compaz,8,3,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["si"],compaz,4,2,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["sol#"],compaz,1,2,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["sol#"],compaz,2,2,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["do"],compaz,4,2,ondaSilencio)

lead2_parte1 = melody(lead2_parte1,notas_musicales["la"],compaz,8,2,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["sol#"],compaz,8,2,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["fa#"],compaz,2,2,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["fa#"],compaz,4,2,ondaActual)
lead2_parte1 = melody(lead2_parte1,notas_musicales["do"],compaz,4,2,ondaSilencio)

lead2_parte1 = melody(lead2_parte1,notas_musicales["mi"],compaz,4,3,ondaCuadrada)
lead2_parte1 = melody(lead2_parte1,notas_musicales["do"],compaz,4,0,ondaSilencio)
lead2_parte1 = melody(lead2_parte1,notas_musicales["re#"],compaz,4,3,ondaCuadrada)
lead2_parte1 = melody(lead2_parte1,notas_musicales["do"],compaz,4,0,ondaSilencio)

sublead_parte2 = []
ondaActual = ondaSilencio
sublead_parte2 = letmotive1(sublead_parte2,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["mi"],compaz,4,3,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["sol#"],compaz,2,3,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["sol#"],compaz,4,3,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["do"],compaz,4,0,ondaSilencio)

sublead_parte2 = letmotive1(sublead_parte2,ondaActual)

sublead_parte2 = melody(sublead_parte2,notas_musicales["si"],compaz,4,3,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["sol#"],compaz,2,3,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["sol#"],compaz,4,3,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["do"],compaz,4,0,ondaSilencio)

ondaActual = ondaSierra
sublead_parte2 = melody(sublead_parte2,notas_musicales["sol#"],compaz,4,3,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["do"],compaz,4,0,ondaSilencio)
sublead_parte2 = melody(sublead_parte2,notas_musicales["la"],compaz,4,3,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["do"],compaz,4,0,ondaSilencio)

sublead_parte2 = melody(sublead_parte2,notas_musicales["si"],compaz,2,3,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["do"],compaz,4,0,ondaSilencio)
sublead_parte2 = melody(sublead_parte2,notas_musicales["do#"],compaz,4,4,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["mi"],compaz,4,3,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["mi"],compaz,8,3,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["fa#"],compaz,4,3,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["fa#"],compaz,8,3,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["sol#"],compaz,4,3,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["si"],compaz,2,3,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["si"],compaz,4,3,ondaActual)

sublead_parte2 = melody(sublead_parte2,notas_musicales["do#"],compaz,4,4,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["re#"],compaz,4,3,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["re#"],compaz,8,3,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["re#"],compaz,4,4,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["re#"],compaz,8,4,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["si"],compaz,4,3,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["sol#"],compaz,1,3,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["sol#"],compaz,2,3,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["do"],compaz,4,2,ondaSilencio)

sublead_parte2 = melody(sublead_parte2,notas_musicales["la"],compaz,8,3,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["sol#"],compaz,8,3,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["fa#"],compaz,2,3,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["fa#"],compaz,4,3,ondaActual)
sublead_parte2 = melody(sublead_parte2,notas_musicales["do"],compaz,4,2,ondaSilencio)
sublead_parte2 = melody(sublead_parte2,notas_musicales["do"],compaz,4,1,ondaSilencio)

sublead_parte2 = melody(sublead_parte2,notas_musicales["mi"],compaz,4,3,ondaCuadrada)
sublead_parte2 = melody(sublead_parte2,notas_musicales["do"],compaz,4,0,ondaSilencio)
sublead_parte2 = melody(sublead_parte2,notas_musicales["sol#"],compaz,4,3,ondaCuadrada)
sublead_parte2 = melody(sublead_parte2,notas_musicales["do"],compaz,4,0,ondaSilencio)

#Parte 2

lead_parte2 = []
def letmotive2(array,onda):
    array = melody(array,notas_musicales["do#"],compaz,8,3,onda)
    array = melody(array,notas_musicales["mi"],compaz,8,3,onda)
    array = melody(array,notas_musicales["re#"],compaz,8,3,onda)
    array = melody(array,notas_musicales["mi"],compaz,8,3,onda)

    array = melody(array,notas_musicales["do#"],compaz,4,3,onda)
    array = melody(array,notas_musicales["do#"],compaz,8,3,ondaSilencio)

    array = melody(array,notas_musicales["do#"],compaz,4,3,onda)
    array = melody(array,notas_musicales["re#"],compaz,8,3,onda)
    array = melody(array,notas_musicales["mi"],compaz,8,3,onda)
    array = melody(array,notas_musicales["si"],compaz,8,3,onda)
    array = melody(array,notas_musicales["sol#"],compaz,4,3,onda)
    array = melody(array,notas_musicales["do#"],compaz,4,3,ondaSilencio)
    return array

lead_parte2 = letmotive2(lead_parte2,ondaCuadrada)
lead_parte2 = letmotive2(lead_parte2,ondaCuadrada)
lead_parte2 = letmotive2(lead_parte2,ondaCuadrada)

lead_parte2 = melody(lead_parte2,notas_musicales["si"],compaz,8,2,ondaCuadrada)
lead_parte2 = melody(lead_parte2,notas_musicales["si"],compaz,4,2,ondaCuadrada)
lead_parte2 = melody(lead_parte2,notas_musicales["fa#"],compaz,8,3,ondaCuadrada)
lead_parte2 = melody(lead_parte2,notas_musicales["fa#"],compaz,4,3,ondaCuadrada)
lead_parte2 = melody(lead_parte2,notas_musicales["mi"],compaz,4,3,ondaCuadrada)
lead_parte2 = melody(lead_parte2,notas_musicales["re#"],compaz,8,3,ondaCuadrada)
lead_parte2 = melody(lead_parte2,notas_musicales["do#"],compaz,4,3,ondaCuadrada)
lead_parte2 = melody(lead_parte2,notas_musicales["si"],compaz,4,2,ondaCuadrada)
lead_parte2 = melody(lead_parte2,notas_musicales["si"],compaz,8,2,ondaCuadrada)
lead_parte2 = melody(lead_parte2,notas_musicales["re#"],compaz,4,3,ondaCuadrada)

lead_parte2 = np.tile(lead_parte2,2)

lead_parte3 = []
lead_parte3 = letmotive2(lead_parte3,ondaSierra)
lead_parte3 = letmotive2(lead_parte3,ondaSierra)
lead_parte3 = letmotive2(lead_parte3,ondaSierra)

lead_parte3 = melody(lead_parte3,notas_musicales["si"],compaz,8,2,ondaSierra)
lead_parte3 = melody(lead_parte3,notas_musicales["si"],compaz,4,2,ondaSierra)
lead_parte3 = melody(lead_parte3,notas_musicales["fa#"],compaz,8,3,ondaSierra)
lead_parte3 = melody(lead_parte3,notas_musicales["fa#"],compaz,4,3,ondaSierra)
lead_parte3 = melody(lead_parte3,notas_musicales["mi"],compaz,4,3,ondaSierra)
lead_parte3 = melody(lead_parte3,notas_musicales["re#"],compaz,8,3,ondaSierra)
lead_parte3 = melody(lead_parte3,notas_musicales["do#"],compaz,4,3,ondaSierra)
lead_parte3 = melody(lead_parte3,notas_musicales["si"],compaz,4,2,ondaSierra)
lead_parte3 = melody(lead_parte3,notas_musicales["si"],compaz,8,2,ondaSierra)
lead_parte3 = melody(lead_parte3,notas_musicales["re#"],compaz,4,3,ondaSierra)

lead_parte3 = np.tile(lead_parte3,2)

leadA = lead_parte1[:len(sublead_parte1)]+sublead_parte1
leadB = lead2_parte1+sublead_parte2[:len(lead2_parte1)]

chord1 = []

chord1 = acorde(chord1,[notas_musicales["do"],notas_musicales["mi"],notas_musicales["sol"]],compaz,1,3,ondaSeno,v=0.0)
chord1 = acorde(chord1,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,0,2,ondaSeno,v=0.2)
chord1 = acorde(chord1,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,0,2,ondaSeno,v=0.2)
chord1 = acorde(chord1,[notas_musicales["do#"],notas_musicales["mi"],notas_musicales["sol#"]],compaz,0,2,ondaSeno,v=0.2)
chord1 = acorde(chord1,[notas_musicales["do#"],notas_musicales["mi"],notas_musicales["sol#"]],compaz,0,2,ondaSeno,v=0.2)
chord1 = acorde(chord1,[notas_musicales["fa#"],notas_musicales["la"],notas_musicales["do#"]],compaz,0,2,ondaSeno,v=0.2)
chord1 = acorde(chord1,[notas_musicales["sol#"],notas_musicales["si"],notas_musicales["re#"]],compaz,0,2,ondaSeno,v=0.2)
chord1 = acorde(chord1,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,0,2,ondaSeno,v=0.2)
chord1 = acorde(chord1,[notas_musicales["si"],notas_musicales["re#"],notas_musicales["fa#"]],compaz,1,2,ondaSeno,v=0.2)
chord1 = acorde(chord1,[notas_musicales["si"],notas_musicales["re#"],notas_musicales["fa#"]],compaz,1,2,ondaSeno,v=0.2)

chord1 = np.tile(chord1,2)

chord1 = acorde(chord1,[notas_musicales["si"],notas_musicales["re#"],notas_musicales["fa#"]],compaz,1,2,ondaSeno,v=0.0)

chord2 = []
chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,8,2,ondaSeno,v=0.2)
chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,4,2,ondaSeno,v=0.0)
chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,8,2,ondaSeno,v=0.0)
chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,8,2,ondaSeno,v=0.2)
chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,4,2,ondaSeno,v=0.0)
chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,8,2,ondaSeno,v=0.2)
chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,4,2,ondaSeno,v=0.0)
chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,8,2,ondaSeno,v=0.2)
chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,8,2,ondaSeno,v=0.0)
chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["si"]],compaz,8,2,ondaSeno,v=0.2)
chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,4,2,ondaSeno,v=0.0)
chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,8,2,ondaSeno,v=0.0)

chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,8,2,ondaSeno,v=0.2)
chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,4,2,ondaSeno,v=0.0)
chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,8,2,ondaSeno,v=0.0)
chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,8,2,ondaSeno,v=0.2)
chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,4,2,ondaSeno,v=0.0)
chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,8,2,ondaSeno,v=0.2)
chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,4,2,ondaSeno,v=0.0)
chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,8,2,ondaSeno,v=0.2)
chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,8,2,ondaSeno,v=0.0)
chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["si"]],compaz,8,2,ondaSeno,v=0.2)
chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,4,2,ondaSeno,v=0.0)
chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,8,2,ondaSeno,v=0.0)

chord2 = acorde(chord2,[notas_musicales["mi"],notas_musicales["do#"],notas_musicales["sol#"]],compaz,8,2,ondaSeno,v=0.2)
chord2 = acorde(chord2,[notas_musicales["mi"],notas_musicales["do#"],notas_musicales["sol#"]],compaz,4,2,ondaSeno,v=0.0)
chord2 = acorde(chord2,[notas_musicales["mi"],notas_musicales["do#"],notas_musicales["sol#"]],compaz,8,2,ondaSeno,v=0.0)
chord2 = acorde(chord2,[notas_musicales["mi"],notas_musicales["do#"],notas_musicales["sol#"]],compaz,8,2,ondaSeno,v=0.2)
chord2 = acorde(chord2,[notas_musicales["mi"],notas_musicales["do#"],notas_musicales["sol#"]],compaz,4,2,ondaSeno,v=0.0)
chord2 = acorde(chord2,[notas_musicales["mi"],notas_musicales["do#"],notas_musicales["sol#"]],compaz,8,2,ondaSeno,v=0.2)
chord2 = acorde(chord2,[notas_musicales["mi"],notas_musicales["do#"],notas_musicales["sol#"]],compaz,4,2,ondaSeno,v=0.0)
chord2 = acorde(chord2,[notas_musicales["mi"],notas_musicales["do#"],notas_musicales["sol#"]],compaz,8,2,ondaSeno,v=0.2)
chord2 = acorde(chord2,[notas_musicales["mi"],notas_musicales["do#"],notas_musicales["sol#"]],compaz,8,2,ondaSeno,v=0.0)
chord2 = acorde(chord2,[notas_musicales["mi"],notas_musicales["do#"],notas_musicales["sol#"]],compaz,8,2,ondaSeno,v=0.2)
chord2 = acorde(chord2,[notas_musicales["mi"],notas_musicales["do#"],notas_musicales["sol#"]],compaz,4,2,ondaSeno,v=0.0)
chord2 = acorde(chord2,[notas_musicales["mi"],notas_musicales["do#"],notas_musicales["sol#"]],compaz,8,2,ondaSeno,v=0.0)

chord2 = acorde(chord2,[notas_musicales["sol#"],notas_musicales["si"],notas_musicales["re#"]],compaz,1,2,ondaSeno,v=0.2)
chord2 = acorde(chord2,[notas_musicales["la"],notas_musicales["do#"],notas_musicales["mi"]],compaz,1,2,ondaSeno,v=0.2)

onda1 = leadA+chord1[:len(leadA)]
onda2 = leadB+chord1[:len(leadB)]

onda3 = lead_parte2[:len(chord2)]+chord2
onda3 = np.tile(onda3,2)

onda4 = lead_parte3[:len(chord2)]+chord2
onda4 = np.tile(onda4,2)

onda = np.concatenate((onda1,onda2,onda3,onda4))

onda_16bits = (np.array(onda)*32767).astype(np.int16)
wavfile.write(f'./audios/proyecto_01/proyecto_1-SergioPalacios.wav',44100,onda_16bits)