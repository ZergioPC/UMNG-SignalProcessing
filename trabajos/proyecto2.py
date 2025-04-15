"""
PROYECTO NÚMERO #2 -  PROCESAMIENTO DE SEÑALES
Sergio Palacios
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.io import wavfile

def leerAudio(audio:str) -> tuple[int,np.array]:
    ruta = os.path.realpath(__file__)
    data_dir = os.path.join(os.path.dirname(ruta),'proyecto2-audios')
    wav_fname = os.path.join(data_dir, audio)
    return wavfile.read(wav_fname)

#signal = leerAudio("cello-a4.wav")[1]
#signal = leerAudio("clarinet-a4.wav")[1]
#signal = leerAudio("flute-a4.wav")[1]
#signal = leerAudio("harp-a4-ksharp_a4_mf.wav")[1]
#signal = leerAudio("oboe-a4.wav")[1]
#signal = leerAudio("piano-a4-sound.wav")[1]
#signal = leerAudio("sax-soprano-a4.wav")[1]
#signal = leerAudio("trumpet-a4.wav")[1]
signal = leerAudio("violin-a4.wav")[1]

L = 1000    # Muestras
T = 1/1000

# Fast Fourier Transform
yf = fft(signal)
xf = fftfreq(L, T)[:L//2]
# Magnitud, Parte real e imaginaria
magnitude = 2.0/L * np.abs(yf[0:L//2])
real_part = np.real(yf)
imag_part = np.imag(yf)

# Gráfica de Magnitud
plt.plot(xf, magnitude)
plt.grid()
plt.title("Espectro de Magnitud")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.show()

# Grafica Real-Imaginaria
plt.plot(real_part, imag_part)
plt.grid()
plt.title("Señal en el plano Complejo")
plt.xlabel("Real")
plt.ylabel("Imaginaria")
plt.show()