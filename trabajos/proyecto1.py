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

def ondaDrums(T,snare):                 #Crea la onda de un Kick y un Kick/Snare
    Fm = 44100
    onda1 = []
    onda2 = []
    for t in range(int(Fm*T)):
        aux = (np.sin((2*np.pi/Fm)*104*t))
        aux2 = (np.sin((2*np.pi/Fm)*134*t))
        aux2 = 0.4 if(aux2 >0) else -0.4
        onda1.append(aux)
        onda2.append(aux2)
    onda = np.array(onda1)+np.array(onda2) if snare else np.array(onda1)
    nota = np.linspace(1,0,2000)
    kick = np.zeros(len(onda))
    kick[:len(nota)] = nota   
    return onda*kick

def melody(array,nota,bpm,n,octava,onda,v=0.7):
    w = frecuenciaMusical(nota,octava)
    t = tempo(bpm,n)

    return np.concatenate((array,onda(w,t,a=v)))

def drums(bpm,compaces):                #Crea un loop de bateria a 4/4
    t = tempo(bpm,2)
    kick = ondaDrums(t,False)
    snare = ondaDrums(t,True)
    onda = np.concatenate((kick,snare))
    onda = np.tile(onda,2)
    return np.tile(onda,compaces)

"""
CANCIÓN: ASGORE (Undertale OST)
Autor: Toby Fox
"""
compaz = 115
lead = []

#Parte 1
lead_parte1 = []

lead_parte1 = melody(lead_parte1,notas_musicales["do"],compaz,2,0,ondaSilencio)
lead_parte1 = melody(lead_parte1,notas_musicales["do"],compaz,2,0,ondaSilencio)

def letmotive1(array):
    array = melody(array,notas_musicales["mi"],compaz,4,3,ondaCuadrada)
    array = melody(array,notas_musicales["do"],compaz,4,0,ondaSilencio)
    array = melody(array,notas_musicales["sol#"],compaz,4,3,ondaCuadrada)
    array = melody(array,notas_musicales["do"],compaz,4,0,ondaSilencio)

    array = melody(array,notas_musicales["fa#"],compaz,2,3,ondaCuadrada)
    array = melody(array,notas_musicales["do"],compaz,4,0,ondaSilencio)
    array = melody(array,notas_musicales["sol#"],compaz,4,3,ondaCuadrada)
    array = melody(array,notas_musicales["do#"],compaz,4,3,ondaCuadrada)
    array = melody(array,notas_musicales["do#"],compaz,8,3,ondaCuadrada)
    array = melody(array,notas_musicales["re#"],compaz,4,3,ondaCuadrada)
    array = melody(array,notas_musicales["re#"],compaz,8,3,ondaCuadrada)
    return array

lead_parte1 = letmotive1(lead_parte1)
lead_parte1 = melody(lead_parte1,notas_musicales["mi"],compaz,4,3,ondaCuadrada)
lead_parte1 = melody(lead_parte1,notas_musicales["sol#"],compaz,2,3,ondaCuadrada)
lead_parte1 = melody(lead_parte1,notas_musicales["sol#"],compaz,4,3,ondaCuadrada)
lead_parte1 = melody(lead_parte1,notas_musicales["do"],compaz,4,0,ondaSilencio)

lead_parte1 = letmotive1(lead_parte1)

lead_parte1 = melody(lead_parte1,notas_musicales["si"],compaz,4,3,ondaCuadrada)
lead_parte1 = melody(lead_parte1,notas_musicales["sol#"],compaz,2,3,ondaCuadrada)
lead_parte1 = melody(lead_parte1,notas_musicales["sol#"],compaz,4,3,ondaCuadrada)
lead_parte1 = melody(lead_parte1,notas_musicales["do"],compaz,4,0,ondaSilencio)

#Parte 2

lead_parte2 = []
def letmotive2(array):
    array = melody(array,notas_musicales["do#"],compaz,8,3,ondaCuadrada)
    array = melody(array,notas_musicales["mi"],compaz,8,3,ondaCuadrada)
    array = melody(array,notas_musicales["re#"],compaz,8,3,ondaCuadrada)
    array = melody(array,notas_musicales["mi"],compaz,8,3,ondaCuadrada)

    array = melody(array,notas_musicales["do#"],compaz,4,3,ondaCuadrada)
    array = melody(array,notas_musicales["do#"],compaz,8,3,ondaSilencio)

    array = melody(array,notas_musicales["do#"],compaz,4,3,ondaCuadrada)
    array = melody(array,notas_musicales["re#"],compaz,8,3,ondaCuadrada)
    array = melody(array,notas_musicales["mi"],compaz,8,3,ondaCuadrada)
    array = melody(array,notas_musicales["si"],compaz,8,3,ondaCuadrada)
    array = melody(array,notas_musicales["sol#"],compaz,4,3,ondaCuadrada)
    array = melody(array,notas_musicales["do#"],compaz,4,3,ondaSilencio)
    return array

lead_parte2 = letmotive2(lead_parte2)
lead_parte2 = letmotive2(lead_parte2)
lead_parte2 = letmotive2(lead_parte2)

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

#ondak = drums(90)
ondak = lead_parte1
onda_16bits = (np.array(ondak)*32767).astype(np.int16)
wavfile.write(f'./audios/proyecto_01/lead.wav',44100,onda_16bits)