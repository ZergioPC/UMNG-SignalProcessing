"""
Canción: Sinfonía 9. From the new World
Autor: Dvořák
"""

import numpy as np
from guiaFourier_Modulos import FourierMusicalClass

music = FourierMusicalClass()
music.kick = music.normalizar(music.leerAudio("bombo.wav")[1])
music.snare = music.normalizar(music.leerAudio("redoblante.wav")[1])

notas = music.notas
vst = music.instrumentos["trompeta"]
bpm = 150

kick = music.drumClip(music.kick,music.tempo(bpm,2))
kick = [kick[i]*0.6 for i in range(len(kick))]
snare = music.drumClip(music.snare,music.tempo(bpm,2))
snare = [snare[i]*0.6 for i in range(len(snare))]

onda = []
drums = []
compaz = music.tempo(bpm,0)*4
sustain = True

song = []

"""
onda = np.concatenate((onda,kick))
onda = np.concatenate((onda,snare))
onda = np.concatenate((onda,kick))
onda = np.concatenate((onda,snare))
"""
print("compilando inicio")
onda = np.concatenate((onda, music.seriefourier(notas["si"], 1, music.tempo(bpm, 1), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["do"], 2, music.tempo(bpm, 1), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["si"], 1, music.tempo(bpm, 1), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["do"], 2, music.tempo(bpm, 1), vst, 1.0, sustain)))

onda = np.concatenate((onda, music.seriefourier(notas["si"], 1, music.tempo(bpm, 2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["do"], 2, music.tempo(bpm, 2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["si"], 1, music.tempo(bpm, 2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["do"], 2, music.tempo(bpm, 2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["si"], 1, music.tempo(bpm, 2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["do"], 2, music.tempo(bpm, 2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["si"], 1, music.tempo(bpm, 2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["do"], 2, music.tempo(bpm, 2), vst, 1.0, sustain)))

onda = np.concatenate((onda, music.seriefourier(notas["si"], 1, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["do"], 2, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["si"], 1, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["do#"], 2, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["si"], 1, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["re#"], 2, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["si"], 1, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["mi"], 2, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["si"], 1, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["fa#"], 2, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["si"], 1, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["sol"], 2, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["si"], 1, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["la"], 2, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["do"], 2, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["la#"], 2, music.tempo(bpm, 4), vst, 1.0, sustain)))

for _ in range(3):
    onda = np.concatenate((onda, music.seriefourier(notas["si"], 2, music.tempo(bpm,8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["si"], 1, music.tempo(bpm,8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["re#"], 2, music.tempo(bpm,8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["fa#"], 2, music.tempo(bpm,8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["do"], 3, music.tempo(bpm,2), vst, 1.0, sustain)))

onda = np.concatenate((onda, music.seriefourier(notas["si"], 2, music.tempo(bpm,8), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["si"], 1, music.tempo(bpm,8), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["re#"], 2, music.tempo(bpm,8), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["fa#"], 2, music.tempo(bpm,8), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["re#"], 3, music.tempo(bpm,1), vst, 1.0, sustain)))

onda = np.concatenate((onda, music.seriefourier(notas["re#"], 3, music.tempo(bpm,2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["re#"], 3, music.tempo(bpm,2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["re#"], 3, music.tempo(bpm,2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["re#"], 3, music.tempo(bpm,2), vst, 1.0, sustain)))

for _ in range(8):
    onda = np.concatenate((onda, music.seriefourier(notas["re#"], 3, music.tempo(bpm,4), vst, 1.0, sustain)))

song = np.concatenate((song,onda))

#Melodía Principal
print("compilando melodia Principal")
onda = []
onda = np.concatenate((onda, music.seriefourier(notas["mi"], 2, music.tempo(bpm, 1), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["fa#"], 2, music.tempo(bpm, 2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["sol"], 2, music.tempo(bpm, 2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["fa#"], 2, music.tempo(bpm, 3), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["mi"], 2, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["mi"], 2, music.tempo(bpm, 1), vst, 1.0, sustain)))

onda = np.concatenate((onda, music.seriefourier(notas["mi"], 2, music.tempo(bpm, 1), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["re"], 2, music.tempo(bpm, 2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["si"], 1, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["re"], 2, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["mi"], 2, music.tempo(bpm, 0), vst, 1.0, sustain)))

drums = np.concatenate((drums, music.drumClip(kick,music.tempo(bpm,1))))
drums = np.concatenate((drums, music.drumClip(snare,music.tempo(bpm,1))))
drums = np.concatenate((drums, music.drumClip(kick,music.tempo(bpm,3))))
drums = np.concatenate((drums, music.drumClip(kick,music.tempo(bpm,4))))
drums = np.concatenate((drums, music.drumClip(snare,music.tempo(bpm,1))))

drums = np.concatenate((drums, music.drumClip(kick,music.tempo(bpm,1))))
drums = np.concatenate((drums, music.drumClip(kick,music.tempo(bpm,3))))
drums = np.concatenate((drums, music.drumClip(kick,music.tempo(bpm,4))))
drums = np.concatenate((drums, music.drumClip(kick,music.tempo(bpm,1))))
drums = np.concatenate((drums, music.drumClip(snare,music.tempo(bpm,1))))

mix = music.normalizar([drums[i]+onda[i] for i in range(int(compaz*music.FM))])
song = np.concatenate((song,mix))

onda = []
onda = np.concatenate((onda, music.seriefourier(notas["mi"], 2, music.tempo(bpm, 1), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["fa#"], 2, music.tempo(bpm, 2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["sol"], 2, music.tempo(bpm, 2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["fa#"], 2, music.tempo(bpm, 3), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["mi"], 2, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["mi"], 2, music.tempo(bpm, 1), vst, 1.0, sustain)))

onda = np.concatenate((onda, music.seriefourier(notas["mi"], 2, music.tempo(bpm, 2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["mi"], 2, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["sol"], 2, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["si"], 2, music.tempo(bpm, 2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["re#"], 2, music.tempo(bpm, 2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["mi"], 2, music.tempo(bpm, 0), vst, 1.0, sustain)))

mix = music.normalizar([drums[i]+onda[i] for i in range(int(compaz*music.FM))])
song = np.concatenate((song,mix))

#Melodia Principal 2
print("compilando melodía principal octavada")
onda = []
onda = np.concatenate((onda, music.seriefourier(notas["mi"], 3, music.tempo(bpm, 1), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["fa#"], 3, music.tempo(bpm, 2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["sol"], 3, music.tempo(bpm, 2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["fa#"], 3, music.tempo(bpm, 3), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["mi"], 3, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["mi"], 3, music.tempo(bpm, 1), vst, 1.0, sustain)))

onda = np.concatenate((onda, music.seriefourier(notas["mi"], 3, music.tempo(bpm, 1), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["re"], 3, music.tempo(bpm, 2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["si"], 2, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["re"], 3, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["mi"], 3, music.tempo(bpm, 0), vst, 1.0, sustain)))

mix = music.normalizar([drums[i]+onda[i] for i in range(int(compaz*music.FM))])
song = np.concatenate((song,mix))

onda = []
onda = np.concatenate((onda, music.seriefourier(notas["mi"], 3, music.tempo(bpm, 1), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["fa#"], 3, music.tempo(bpm, 2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["sol"], 3, music.tempo(bpm, 2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["fa#"], 3, music.tempo(bpm, 3), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["mi"], 3, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["mi"], 3, music.tempo(bpm, 1), vst, 1.0, sustain)))

onda = np.concatenate((onda, music.seriefourier(notas["mi"], 3, music.tempo(bpm, 2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["mi"], 3, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["sol"], 3, music.tempo(bpm, 4), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["si"], 3, music.tempo(bpm, 2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["re#"], 3, music.tempo(bpm, 2), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["mi"], 3, music.tempo(bpm, 0), vst, 1.0, sustain)))

mix = music.normalizar([drums[i]+onda[i] for i in range(int(compaz*music.FM))])
song = np.concatenate((song,mix))

# ENDING
print("compilando ending")
onda=[]
for _ in range(4):
    onda = np.concatenate((onda, music.seriefourier(notas["mi"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["fa#"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["sol"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["la"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))

    onda = np.concatenate((onda, music.seriefourier(notas["la#"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["si"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["do#"], 3, music.tempo(bpm, 8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["re#"], 3, music.tempo(bpm, 8), vst, 1.0, sustain)))

    onda = np.concatenate((onda, music.seriefourier(notas["mi"], 3, music.tempo(bpm, 8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["re#"], 3, music.tempo(bpm, 8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["do#"], 3, music.tempo(bpm, 8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["si"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))

    onda = np.concatenate((onda, music.seriefourier(notas["la#"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["la"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["sol"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["fa#"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))

mix = music.normalizar([drums[i]+onda[i] for i in range(int(compaz*music.FM))])
song = np.concatenate((song,mix))

onda=[]
for _ in range(3):
    onda = np.concatenate((onda, music.seriefourier(notas["mi"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["fa#"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["sol"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["la"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))

    onda = np.concatenate((onda, music.seriefourier(notas["la#"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["si"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["do#"], 3, music.tempo(bpm, 8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["re#"], 3, music.tempo(bpm, 8), vst, 1.0, sustain)))

    onda = np.concatenate((onda, music.seriefourier(notas["mi"], 3, music.tempo(bpm, 8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["re#"], 3, music.tempo(bpm, 8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["do#"], 3, music.tempo(bpm, 8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["si"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))

    onda = np.concatenate((onda, music.seriefourier(notas["la#"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["la"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["sol"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))
    onda = np.concatenate((onda, music.seriefourier(notas["fa#"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))

onda = np.concatenate((onda, music.seriefourier(notas["mi"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["fa#"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["sol"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["la"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))

onda = np.concatenate((onda, music.seriefourier(notas["la#"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["si"], 2, music.tempo(bpm, 8), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["do#"], 3, music.tempo(bpm, 8), vst, 1.0, sustain)))
onda = np.concatenate((onda, music.seriefourier(notas["re#"], 3, music.tempo(bpm, 8), vst, 1.0, sustain)))

onda = np.concatenate((onda, music.seriefourier(notas["mi"], 3, music.tempo(bpm, 0), vst, 1.0, sustain)))

mix = music.normalizar([drums[i]+onda[i] for i in range(int(compaz*music.FM))])
song = np.concatenate((song,mix))

music.renderAudio(song,"canción_1_trompeta")
