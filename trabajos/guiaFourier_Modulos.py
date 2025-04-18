import os
import numpy as np
from scipy.io import wavfile

class FourierMusicalClass:
    """
    Clase que facilie la creación de música básica mediante 
    el procesamiento de señales
    """
    def __init__(self) -> None:
        self.FM = 44100
        self.notas = {
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
        self.instrumentos = {
            "violin":[66,63,65,56,58,66,55,54,60,56,54,45,40,38,46],
            "trompeta":[63,66,70,66,56,50,47,44],
            "arpa":[65,40,50]
        }
        self.kick = []
        self.snare = []

        # FUNCIONES AUXILIARES

    def leerAudio(self, audio:str) -> tuple[list, list]:
        ruta = os.path.realpath(__file__)
        data_dir = os.path.join(os.path.dirname(ruta),'guiaFourier-audios')
        wav_fname = os.path.join(data_dir, audio)
        return wavfile.read(wav_fname)

    def normalizar(self, lista:list) -> list[float]:
        """
        Normaliza la lista manualmente
        """
        max = 0
        for n in lista:
            if ( np.abs(n) > max):
                max = n
        return [(n/max)*0.99 for n in lista]

    # FUNCIONES MUSICALES

    def frecuenciaMusical(self, nota:float, octava:int) -> float:
        """ 
        Retorna la frecuencia de la nota musical según
        la octava
        """
        return (nota)*(2**(octava+1))

    def tempo(self, bpm:float, n:int) -> float:
        """
        Retorna la duración de la nota según
        la notación músical y el BPM.
        0: Redonda
        1: Blanca
        2: Negra
        3: Negra con Puntillo
        4: Corchea
        5: Corchea con Puntillo
        8: Semicorchea
        Sí el compáz es a 3/4, agregar un 1 al principio : 10 u 11 ..
        """
        if(n==0):
            tiempo = (4*(44100*60))/bpm
        elif(n==1):
            tiempo = (2*(44100*60))/bpm
        elif(n==2):
            tiempo = ((44100*60))/bpm
        elif(n==3):
            tiempo = 60*((44100)+(0.5*44100))/bpm
        elif(n==4):
            tiempo = (0.5*(44100*60))/bpm
        elif(n==5):
            tiempo = 60*((0.5*44100)+(0.25*44100))/bpm
        elif(n==8):
            tiempo = (0.25*(44100*60))/bpm
        elif(n==9):
            tiempo = (0.125*(44100*60))/bpm
        elif(n==10):
            tiempo = (4*(44100*80))/bpm
        elif(n==11):
            tiempo = (2*(44100*80))/bpm
        elif(n==12):
            tiempo = ((44100*80))/bpm
        elif(n==13):
            tiempo = 80*((44100)+(0.5*44100))/bpm
        elif(n==14):
            tiempo = (0.5*(44100*80))/bpm
        elif(n==15):
            tiempo = 80*((0.5*44100)+(0.25*44100))/bpm
        elif(n==18):
            tiempo = (0.25*(44100*80))/bpm
        
        return tiempo/self.FM

    def seriefourier(self, nota:float,  octava:int,  T:float,  instrumento:list,  vol:float=1, sustain:bool=True) -> list[float]:
        """ 
        Serie de Armónicos de Fourier para obtener el
        timbre de un instrumento
        """
        serie = []
        freq = self.frecuenciaMusical(nota,octava)

        for t in range(int(self.FM*T)):
            suma = 0
            for n in range(len(instrumento)):
                suma += instrumento[n]*np.sin(n*(2*np.pi/self.FM)*freq*t)
            
            if not sustain:
                suma += (1/(1*np.e**7*(t-0.5))) if (t > 0) else 0 
            serie.append(suma)

        maxValue = max(serie)
        return [(x/maxValue)*vol for x in serie]

    def drumClip(self, wav:list, BPM:float) -> list:
        """ 
        Ajusta la duración de la percución según el BMM
        """
        audio = []
        if(len(wav) < int(self.FM*BPM)):
            audio = np.concatenate((wav,[0 for i in range(int(BPM*self.FM) - len(wav))]))
        else:
            audio = wav[:int(self.FM*BPM)]
        return audio
    
    # EXPORTAR AUDIO

    def renderAudio(self, onda:list, nombre:str) -> None:
        """ 
        Guarda el audio en un archivo.wav
        """
        print("Renderizando . . .")
        onda_16bits = (np.array(onda)*32767).astype(np.int16)
        wavfile.write(f"./audios/guiaForuier/{nombre}.wav", self.FM, onda_16bits)
