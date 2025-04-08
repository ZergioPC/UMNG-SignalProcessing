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
vst = music.instrumentos["violin"]
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

# ARPEGIO
def generarArpegioBase() -> list[float]:
    a = []
    a = np.concatenate((a,music.seriefourier(notas["si"],3,music.tempo(bpm,18),piano,0.06,False)))
    a = np.concatenate((a,music.seriefourier(notas["do#"],4,music.tempo(bpm,18),piano,0.12,False)))
    a = np.concatenate((a,music.seriefourier(notas["fa#"],4,music.tempo(bpm,18),piano,0.18,False)))
    return a

def generarArpegioCustom(n1:float, o1:int, n2:float, o2:int, n3:float, o3:int) -> list[float]:
    a = []
    a = np.concatenate((a,music.seriefourier(n1,o1,music.tempo(bpm,14),piano,0.06,False)))
    a = np.concatenate((a,music.seriefourier(n2,o2,music.tempo(bpm,18),piano,0.08,False)))
    a = np.concatenate((a,music.seriefourier(n3,o3,music.tempo(bpm,15),piano,0.10,False)))
    return a

song = []
#   INTRO
print("Compilando Intro")

arpegio = generarArpegioBase()

for _ in range(16):
    onda_arp = np.concatenate((onda_arp,arpegio))

song = np.concatenate((song,onda_arp))

onda = np.concatenate((onda,music.seriefourier(notas["re#"],1,music.tempo(bpm,1),vst,0.6,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["re#"],2,music.tempo(bpm,1),vst,0.4,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["mi"],1,music.tempo(bpm,1),vst,0.6,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["mi"],2,music.tempo(bpm,1),vst,0.4,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["fa#"],1,music.tempo(bpm,1),vst,0.6,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["fa#"],2,music.tempo(bpm,1),vst,0.4,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["fa#"],2,music.tempo(bpm,1),vst,0.35,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["fa#"],2,music.tempo(bpm,2),vst,0.3,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["mi"],2,music.tempo(bpm,2),vst,0.2,sustain)))

mix = music.normalizar([onda_arp[i]+onda[i] for i in range(int(compaz*music.FM))])
song = np.concatenate((song,mix))
song = np.concatenate((song,mix))

onda_arp = []
onda_arp = np.concatenate((onda_arp,music.seriefourier(notas["fa#"],1,music.tempo(bpm,18),piano,0.06,False)))
onda_arp = np.concatenate((onda_arp,music.seriefourier(notas["do#"],2,music.tempo(bpm,18),piano,0.1,False)))
onda_arp = np.concatenate((onda_arp,music.seriefourier(notas["fa#"],2,music.tempo(bpm,18),piano,0.18,False)))

onda_arp = np.concatenate((onda_arp,music.seriefourier(notas["si"],2,music.tempo(bpm,18),piano,0.1,False)))
onda_arp = np.concatenate((onda_arp,music.seriefourier(notas["fa#"],3,music.tempo(bpm,18),piano,0.06,False)))
onda_arp = np.concatenate((onda_arp,music.seriefourier(notas["do#"],4,music.tempo(bpm,18),piano,0.1,False)))

onda_arp = np.concatenate((onda_arp,music.seriefourier(notas["si"],4,music.tempo(bpm,1),piano,0.1,False)))

drums = np.concatenate((drums,music.drumClip(kick,music.tempo(bpm,2))))
drums = np.concatenate((drums,music.drumClip(kick,music.tempo(bpm,2))))
drums = np.concatenate((drums,music.drumClip(kick,music.tempo(bpm,2))))
drums = np.concatenate((drums,music.drumClip(snare,music.tempo(bpm,18))))
drums = np.concatenate((drums,music.drumClip(snare,music.tempo(bpm,18))))
drums = np.concatenate((drums,music.drumClip(snare,music.tempo(bpm,18))))


mix = music.normalizar([onda_arp[i]+drums[i] for i in range(int(music.tempo(bpm,0)*music.FM))])
song = np.concatenate((song,mix))

#   MELODÍA 1
print("Compilando Melodía 1")

onda = []
onda_arp = []
drums = []

onda = np.concatenate((onda,music.seriefourier(notas["fa#"],3,music.tempo(bpm,18),vst,0.6,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["fa#"],3,music.tempo(bpm,18),vst,0.5,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["fa#"],3,music.tempo(bpm,18),vst,0.55,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["fa#"],3,music.tempo(bpm,14),vst,0.6,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["fa#"],3,music.tempo(bpm,18),vst,0.5,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["fa#"],3,music.tempo(bpm,14),vst,0.6,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["mi"],3,music.tempo(bpm,18),vst,0.5,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["re#"],3,music.tempo(bpm,14),vst,0.6,sustain)))

onda = np.concatenate((onda,music.seriefourier(notas["do#"],3,music.tempo(bpm,18),vst,0.5,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["si"],2,music.tempo(bpm,14),vst,0.6,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["si"],2,music.tempo(bpm,18),vst,0.5,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["si"],2,music.tempo(bpm,14),vst,0.6,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["do#"],3,music.tempo(bpm,18),vst,0.5,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["re#"],3,music.tempo(bpm,14),vst,0.6,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["do#"],3,music.tempo(bpm,18),vst,0.5,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["do#"],3,music.tempo(bpm,2),vst,0.5,sustain)))

onda = np.concatenate((onda,music.seriefourier(notas["fa#"],3,music.tempo(bpm,18),vst,0.6,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["fa#"],3,music.tempo(bpm,18),vst,0.5,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["fa#"],3,music.tempo(bpm,18),vst,0.55,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["fa#"],3,music.tempo(bpm,14),vst,0.6,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["fa#"],3,music.tempo(bpm,18),vst,0.5,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["fa#"],3,music.tempo(bpm,14),vst,0.6,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["mi"],3,music.tempo(bpm,18),vst,0.5,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["re#"],3,music.tempo(bpm,14),vst,0.6,sustain)))

onda = np.concatenate((onda,music.seriefourier(notas["re#"],3,music.tempo(bpm,18),vst,0.4,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["re#"],3,music.tempo(bpm,12),vst,0.6,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["do#"],3,music.tempo(bpm,18),vst,0.5,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["si"],2,music.tempo(bpm,18),vst,0.4,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["do#"],3,music.tempo(bpm,1),vst,0.6,sustain)))

for _ in range(7):
    drums = np.concatenate((drums,music.drumClip(kick,music.tempo(bpm,2))))

drums = np.concatenate((drums,music.drumClip(snare,music.tempo(bpm,18))))
drums = np.concatenate((drums,music.drumClip(snare,music.tempo(bpm,18))))
drums = np.concatenate((drums,music.drumClip(snare,music.tempo(bpm,18))))

drums = np.concatenate((drums,drums))

aux_arp_re = generarArpegioCustom(notas["re#"],1,notas["re#"],2,notas["si"],2)
aux_arp_mi = generarArpegioCustom(notas["mi"],1,notas["mi"],2,notas["sol#"],2)
aux_arp_fa = generarArpegioCustom(notas["fa#"],1,notas["fa#"],2,notas["do#"],3)
aux_arp_sol = generarArpegioCustom(notas["sol#"],1,notas["sol#"],2,notas["re#"],3)
aux_arp_si = generarArpegioCustom(notas["si"],1,notas["si"],2,notas["re#"],3)

onda_arp = np.concatenate((onda_arp,aux_arp_re))
onda_arp = np.concatenate((onda_arp,aux_arp_mi))
onda_arp = np.concatenate((onda_arp,aux_arp_fa))
onda_arp = np.concatenate((onda_arp,aux_arp_fa))
onda_arp = np.concatenate((onda_arp,aux_arp_fa))
onda_arp = np.concatenate((onda_arp,aux_arp_sol))
onda_arp = np.concatenate((onda_arp,aux_arp_mi))
onda_arp = np.concatenate((onda_arp,aux_arp_re))

mix = music.normalizar([onda_arp[i]+onda[i]+drums[i] for i in range(int(compaz*music.FM))])
song = np.concatenate((song,mix))

#   MELODÍA 2
print("Compilando Melodía 2")

onda = []
onda_arp = []
drums = []

onda = np.concatenate((onda,music.seriefourier(notas["si"],3,music.tempo(bpm,14),vst,0.6,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["do#"],4,music.tempo(bpm,18),vst,0.4,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["re#"],4,music.tempo(bpm,14),vst,0.5,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["mi"],4,music.tempo(bpm,15),vst,0.6,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["re#"],4,music.tempo(bpm,18),vst,0.4,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["si"],3,music.tempo(bpm,14),vst,0.5,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["si"],3,music.tempo(bpm,15),vst,0.6,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["re#"],4,music.tempo(bpm,18),vst,0.4,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["si"],3,music.tempo(bpm,14),vst,0.5,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["do#"],4,music.tempo(bpm,1),vst,0.6,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["do#"],4,music.tempo(bpm,18),vst,0.0,sustain)))

onda = np.concatenate((onda,music.seriefourier(notas["si"],3,music.tempo(bpm,14),vst,0.6,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["do#"],4,music.tempo(bpm,18),vst,0.4,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["re#"],4,music.tempo(bpm,14),vst,0.5,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["mi"],4,music.tempo(bpm,15),vst,0.6,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["re#"],4,music.tempo(bpm,18),vst,0.4,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["mi"],4,music.tempo(bpm,14),vst,0.5,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["fa#"],4,music.tempo(bpm,15),vst,0.6,sustain)))

onda = np.concatenate((onda,music.seriefourier(notas["mi"],4,music.tempo(bpm,18),vst,0.4,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["re#"],4,music.tempo(bpm,14),vst,0.5,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["do#"],4,music.tempo(bpm,18),vst,0.4,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["do#"],4,music.tempo(bpm,14),vst,0.6,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["re#"],4,music.tempo(bpm,18),vst,0.4,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["do#"],4,music.tempo(bpm,14),vst,0.6,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["si"],3,music.tempo(bpm,18),vst,0.4,sustain)))

for _ in range(3):
    drums = np.concatenate((drums,music.drumClip(kick,music.tempo(bpm,2))))
    drums = np.concatenate((drums,music.drumClip(snare,music.tempo(bpm,2))))

drums = np.concatenate((drums,music.drumClip(kick,music.tempo(bpm,2))))
drums = np.concatenate((drums,music.drumClip(snare,music.tempo(bpm,18))))
drums = np.concatenate((drums,music.drumClip(snare,music.tempo(bpm,18))))
drums = np.concatenate((drums,music.drumClip(snare,music.tempo(bpm,18))))

drums = np.concatenate((drums,drums))

onda_arp = np.concatenate((onda_arp,aux_arp_sol))
onda_arp = np.concatenate((onda_arp,aux_arp_mi))
onda_arp = np.concatenate((onda_arp,aux_arp_si))
onda_arp = np.concatenate((onda_arp,aux_arp_fa))

onda_arp = np.concatenate((onda_arp,aux_arp_sol))
onda_arp = np.concatenate((onda_arp,aux_arp_mi))
onda_arp = np.concatenate((onda_arp,aux_arp_si))
onda_arp = np.concatenate((onda_arp,aux_arp_fa))

mix = music.normalizar([onda_arp[i]+onda[i]+drums[i] for i in range(int(compaz*music.FM))])
song = np.concatenate((song,mix))

# ENDING
print("Compilando Ending")

onda = []
onda_arp = []
drums = []

onda = np.concatenate((onda,music.seriefourier(notas["si"],3,music.tempo(bpm,0),vst,0.4,sustain)))
onda = np.concatenate((onda,music.seriefourier(notas["fa#"],3,music.tempo(bpm,0),vst,0.5,sustain)))

for _ in range(8):
    onda_arp = np.concatenate((onda_arp,arpegio))

for _ in range(3):
    drums = np.concatenate((drums,music.drumClip(kick,music.tempo(bpm,14))))
    drums = np.concatenate((drums,music.drumClip(snare,music.tempo(bpm,14))))
    drums = np.concatenate((drums,music.drumClip(snare,music.tempo(bpm,14))))

for _ in range(2):
    drums = np.concatenate((drums,music.drumClip(kick,music.tempo(bpm,18))))
    drums = np.concatenate((drums,music.drumClip(snare,music.tempo(bpm,18))))
    drums = np.concatenate((drums,music.drumClip(snare,music.tempo(bpm,18))))

mix = music.normalizar([onda_arp[i]+onda[i]+drums[i] for i in range(int((compaz/2)*music.FM))])
song = np.concatenate((song,mix))

music.renderAudio(song,"canción_2_violin")