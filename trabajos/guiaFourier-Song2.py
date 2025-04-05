"""
Canción: Sparkle
Autor: Radwimps
"""

import numpy as np
from guiaFourier_Modulos import FourierMusicalClass

music = FourierMusicalClass()
music.kick = music.normalizar(music.leerAudio("bombo.wav")[1])
music.snare = music.normalizar(music.leerAudio("redoblante.wav")[1])

notas = music.notas
piano = music.instrumentos["arpa"]
vst = music.instrumentos["trompeta"]
bpm = 125

kick = music.drumClip(music.kick,music.tempo(bpm,2))
kick = [kick[i]*0.6 for i in range(len(kick))]
snare = music.drumClip(music.snare,music.tempo(bpm,2))
snare = [snare[i]*0.6 for i in range(len(snare))]

onda = []
onda_arp = []
drums = []
compaz = music.tempo(bpm,0)*4
sustain = True

song = []

# ARPEGIO
def arpegio():
    a = []
    a = np.concatenate((a,music.seriefourier(notas["si"],3,music.tempo(bpm,18),piano,0.1,False)))
    a = np.concatenate((a,music.seriefourier(notas["do#"],4,music.tempo(bpm,18),piano,0.1,False)))
    a = np.concatenate((a,music.seriefourier(notas["fa#"],4,music.tempo(bpm,18),piano,0.1,False)))
    return a

onda_arp = np.concatenate((onda_arp,arpegio()))
onda_arp = np.concatenate((onda_arp,arpegio()))
onda_arp = np.concatenate((onda_arp,arpegio()))
onda_arp = np.concatenate((onda_arp,arpegio()))

#mix = music.normalizar([drums[i]+onda[i] for i in range(int(compaz*music.FM))])
#song = np.concatenate((song,mix))

music.renderAudio(onda_arp,"canción_2_trompeta")