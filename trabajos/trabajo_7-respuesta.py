"""
TALLER EN CLASE SEMANA 7 -  PROCESAMIENTO DE SEÑALES
Sergio Palacios

Abrir los archivos, para los archivos estéreo solo tomar los datos correspondientes al lado izquierdo(0)

A partir de los audios entregados se deben recortar y crear un audio nuevo con la frase "Welcome To Our House".
para esto se debe recortar de la siguiente manera:
    Archivo Welcome.wav: de este archivo se extrae la palabra "welcome"
    Archivo WelcomeToOurHouse: de este archivo se debe extraer las palabras "to Our"
    Archivo ThisIsHouse: de este archivo se debe extraer las palabras "ThisIs"
Al archivo de audio obtenido con la frase "Welcome To Our house" se debe sumar el canal L del archivo "drum.wav"
con una atenuación de -6dBFS(tenga en cuenta que se esta pidiendo una atenuación y no dejar el nivel pico en -6dBFS)
    Exportar el archivo resultante como un archivo .wav monofónico.

Realizar el mismo procedimiento anterior pero en este caso construir un archivo estereofónico en el cual la frase "welcome To Our House" se encuentre alternada de la siguiente manera:
    L:"Welcome         House"
    R:"        To Our       "
Al archivo de audio estereofónico obtenido con la frase "Welcome To Our house" se debe sumar el archivo "drum.wav"
con una atenuación de -8dBFS(tenga en cuenta que se esta pidiendo una atenuación y no dejar el nivel pico en -6dBFS

Exportar el archivo resultante como un archivo .wav estereofónico.

Se deben entregar los dos archivos .wav obtenidos y el código usado para este proceso.
"""

import numpy as np
import os.path
import matplotlib.pyplot as plt
from scipy.io import wavfile

#   FUNCIONES

def graficar(data,render):
    if render:
        plt.figure(num="Taller #7 - Sergio Palacios")
        plt.title("prueba para saber donde está la palabra")
        plt.xlabel('Tiempo')
        plt.ylabel("audio")
        plt.plot([n for n in range(len(data))],data) 
        plt.show()

def leerAudio(audio):
    ruta = os.path.realpath(__file__)
    data_dir = os.path.join(os.path.dirname(ruta),'trabajo_7-audios')
    wav_fname = os.path.join(data_dir, audio)
    return wavfile.read(wav_fname)

def DBtoBYTE(db):
    return 10**(db/10)

def normalizar(lista):
    max = 0
    for n in lista:
        if ( np.abs(n) > max):
            max = n
    return [(n/max)*0.8 for n in lista]

def renderAudio(onda,name):
    onda_16bits = (np.array(onda)*32767).astype(np.int16)
    wavfile.write(f'./audios/trabajo_07/{name}.wav',44100,onda_16bits)

""" SOLUCIÓN """
fm = 44100

# Lectura de archivos de audio
_ , data_drum =leerAudio("drum.wav")
_ , data_thisIsHouse =leerAudio("ThisIsHouse.wav")
_ , data_welcome =leerAudio("Welcome.wav")
_ , data_welcomeToOurHouse =leerAudio("WelcomeToOurHouse.wav")

# Obtención del canal Izquierdo
data_drum = [n[0] for n in data_drum]
data_thisIsHouse = [n[0] for n in data_thisIsHouse]
data_welcome = [n[0] for n in data_welcome]

#   Normalización
data_drum = normalizar(data_drum)
data_thisIsHouse = normalizar(data_thisIsHouse)
data_welcome = normalizar(data_welcome)
data_welcomeToOurHouse = normalizar(data_welcomeToOurHouse)

# PRIMERA PARTE
graficar(data_welcome,False)            # Hallar la sección para saber donde recortar el audio
audio_welcome = data_welcome[:49000]

graficar(data_welcomeToOurHouse,False)  # Hallar la sección para saber donde recortar el audio
audio_toOur = data_welcomeToOurHouse[30000:55000]

graficar(data_thisIsHouse,False)        # Hallar la sección para saber donde recortar el audio
audio_house = data_thisIsHouse[18000:]

seisDb = DBtoBYTE(-6)

drum6db = [seisDb*n for n in data_drum]
drum6db = normalizar(drum6db)
audio_Mix1 = audio_welcome + audio_toOur + audio_house + drum6db

# SEGUNDA PARTE
graficar(data_welcomeToOurHouse,False)  # Hallar la sección para saber donde recortar el audio

estereo_welcome = data_welcomeToOurHouse[7200:30760]
estereo_toOur = data_welcomeToOurHouse[30760:55900]
estereo_house = data_welcomeToOurHouse[55900:]

estereo_welcome = [[n,0] for n in estereo_welcome]
estereo_toOur = [[0,n] for n in estereo_toOur]
estereo_house = [[n,0] for n in estereo_house]

ochoDb = DBtoBYTE(-8)

drum8db = [ochoDb*n for n in data_drum]
drum8db = normalizar(drum8db)
drum8db = [[n,n] for n in drum8db]

audio_estereo = estereo_welcome + estereo_toOur + estereo_house + drum8db

renderAudio(audio_Mix1,"toOurDrum")
renderAudio(audio_estereo,"welcomeToOurHouseEstereo")