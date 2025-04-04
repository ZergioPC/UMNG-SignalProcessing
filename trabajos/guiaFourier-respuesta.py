import numpy as np
from scipy.io import wavfile

# VARIABLES
FM =44100

notas = {
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

amplitudes = {
    "violin":[66,63,65,56,58,66,55,54,60,56,54,45,40,38,46],
    "trompet":[63,66,70,66,56,50,47,44],
    "arpa":[65,40,50]
}

# FUNCIONES

def frecuenciaMusical(nota,octava):
    return (nota)*(2**(octava+1))

def tempo(bpm,n):
    global FM

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
    
    return tiempo/FM

def seriefourier(nota:float, octava:int, T:int, instrumento:list, vol:int=1,sustain:bool=True):
    global FM
    
    serie = []
    freq = frecuenciaMusical(nota,octava)

    for t in range(FM*T):
        suma = 0
        for n in range(len(instrumento)):
            suma += instrumento[n]*np.sin(n*(2*np.pi/FM)*freq*t)
        
        if not sustain:
            suma = suma*(FM-(np.log10(30*t**4))) if (30*t**4 > 0) else 0 
        serie.append(suma)

    maxValue = max(serie)
    return [(x/maxValue)*vol*0.9 for x in serie]


onda = seriefourier(notas["do"],2,2,amplitudes['arpa'],0.8,False)
onda_16bits = (np.array(onda)*32767).astype(np.int16)
wavfile.write(f"./audios/guiaForuier/test.wav",FM,onda_16bits)