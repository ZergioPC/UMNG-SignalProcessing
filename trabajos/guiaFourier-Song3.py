"""
Canción: Gary vs David
Autor: Owen Dennis (Regular Show OST)
"""

import numpy as np
from guiaFourier_Modulos import FourierMusicalClass

music = FourierMusicalClass()
music.kick = music.normalizar(music.leerAudio("bombo.wav")[1])
music.snare = music.normalizar(music.leerAudio("redoblante.wav")[1])

notas = music.notas
bajo = music.instrumentos["arpa"]
vst1 = music.instrumentos["violin"]
vst2 = music.instrumentos["trompeta"]
bpm = 115

kick = music.drumClip(music.kick,music.tempo(bpm,2))
kick = [kick[i]*0.6 for i in range(len(kick))]
snare = music.drumClip(music.snare,music.tempo(bpm,2))
snare = [snare[i]*0.6 for i in range(len(snare))]

onda1 = []
onda2 = []
bass = []
drums = []
song = []

compaz = music.tempo(bpm,0)*4
sustain = True

def generarBajo(nota:float, octava:int) -> list:
    a =[]
    for vol in range(4):
        a = np.concatenate((a,music.seriefourier(nota,octava,music.tempo(bpm,8),bajo,0.2*((vol+1)/4),False)))
    return a

bajo_re = generarBajo(notas["re"],1)
bajo_sib = generarBajo(notas["la#"],0)
bajo_do = generarBajo(notas["do"],1)
bajo_fa = generarBajo(notas["fa"],0)
bajo_la = generarBajo(notas["la"],0)

#   INTRO
"""
print("Compilando Intro")

for _ in range(32):
    bass = np.concatenate((bass,bajo_re))

drums = np.concatenate((drums,[0 for _ in range(int(music.tempo(bpm,0)*music.FM))]))
drums = np.concatenate((drums,[0 for _ in range(int(music.tempo(bpm,0)*music.FM))]))

for _ in range(9):
    drums = np.concatenate((drums,music.drumClip(kick,music.tempo(bpm,2))))

mix = music.normalizar([bass[i]+drums[i] for i in range(int(compaz*music.FM))])
song = np.concatenate((song,mix))

#   GARY MELODY 1
print("Compilando Gary Melody 1")
bass = []
drums = []

def aux_Letmotive1(n1:float, o1:float, n2:float, o2:float, n3:float, o3:float) -> list:
    a = []
    a = np.concatenate((a,music.seriefourier(n1,o1,music.tempo(bpm,8),vst1,0.5,sustain)))
    a = np.concatenate((a,music.seriefourier(n2,o2,music.tempo(bpm,8),vst1,0.6,sustain)))
    a = np.concatenate((a,music.seriefourier(n3,o3,music.tempo(bpm,8),vst1,0.7,sustain)))
    a = np.concatenate((a,music.seriefourier(n1,o1,music.tempo(bpm,8),vst1,0.5,sustain)))
    a = np.concatenate((a,music.seriefourier(n2,o2,music.tempo(bpm,8),vst1,0.6,sustain)))
    a = np.concatenate((a,music.seriefourier(n3,o3,music.tempo(bpm,8),vst1,0.7,sustain)))
    a = np.concatenate((a,music.seriefourier(n1,o1,music.tempo(bpm,8),vst1,0.5,sustain)))
    a = np.concatenate((a,music.seriefourier(n3,o3,music.tempo(bpm,8),vst1,0.7,sustain)))
    return a

letmotiveA_la1 = aux_Letmotive1(notas["la"],1,notas["re"],2,notas["fa"],2);
letmotiveA_lab = aux_Letmotive1(notas["la#"],1,notas["re"],2,notas["fa"],2);
letmotiveA_sol = aux_Letmotive1(notas["sol"],1,notas["do"],2,notas["mi"],2);
letmotiveA_la2 = aux_Letmotive1(notas["la"],1,notas["do"],2,notas["mi"],2);
letmotiveA_la3 = aux_Letmotive1(notas["la"],1,notas["do"],2,notas["re"],2);
letmotiveA_rev1 = aux_Letmotive1(notas["fa"],3,notas["re"],3,notas["la"],2);
letmotiveA_rev2 = aux_Letmotive1(notas["fa"],3,notas["re"],3,notas["do"],3);
letmotiveA_rev3 = aux_Letmotive1(notas["fa"],3,notas["mi"],3,notas["do"],3);

aux1 = []

for _ in range(4):
    aux1 = np.concatenate((aux1,letmotiveA_la1))
aux1 = np.concatenate((aux1,letmotiveA_lab))
aux1 = np.concatenate((aux1,letmotiveA_sol))
aux1 = np.concatenate((aux1,letmotiveA_la2))
aux1 = np.concatenate((aux1,letmotiveA_la3))
aux1 = np.concatenate((aux1,aux1))

onda1 = np.concatenate((onda1,aux1))

aux2 = []

for _ in range(4):
    aux2 = np.concatenate((aux2,letmotiveA_rev1))
aux2 = np.concatenate((aux2,letmotiveA_rev2))
aux2 = np.concatenate((aux2,letmotiveA_rev2))
aux2 = np.concatenate((aux2,letmotiveA_rev3))
aux2 = np.concatenate((aux2,music.seriefourier(notas["re"],3,music.tempo(bpm,0),vst1,0.6,sustain)))

auxMix = music.normalizar([aux1[i]+aux2[i] for i in range(int(compaz*music.FM))])
onda1 = np.concatenate((onda1,auxMix))

for _ in range(8):
    bass = np.concatenate((bass,bajo_re))
bass = np.concatenate((bass,bajo_sib))
bass = np.concatenate((bass,bajo_sib))
bass = np.concatenate((bass,bajo_do))
bass = np.concatenate((bass,bajo_do))
for _ in range(4):
    bass = np.concatenate((bass,bajo_re))
bass = np.concatenate((bass,bass))
bass = np.concatenate((bass,bass))
bass = np.concatenate((bass,bajo_re))

for _ in range(33):
    drums = np.concatenate((drums,music.drumClip(kick,music.tempo(bpm,2))))
    drums = np.concatenate((drums,music.drumClip(snare,music.tempo(bpm,2))))

mix = music.normalizar([onda1[i]+drums[i]+bass[i] for i in range(len(onda1))])
song = np.concatenate((song,mix))

#   DAVID MELODY 1
print("Compilando David Melody 1")
bass = []
drums = []

onda2 = np.concatenate((onda2,music.seriefourier(notas["la"],3,music.tempo(bpm,4),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["sol"],3,music.tempo(bpm,4),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["fa"],3,music.tempo(bpm,4),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["do"],3,music.tempo(bpm,8),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["sol"],3,music.tempo(bpm,2),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["do"],3,music.tempo(bpm,8),vst2,0.0,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["sol"],3,music.tempo(bpm,8),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["la"],3,music.tempo(bpm,8),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["la#"],3,music.tempo(bpm,8),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["do"],4,music.tempo(bpm,5),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["la#"],3,music.tempo(bpm,4),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["la#"],3,music.tempo(bpm,4),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["do"],4,music.tempo(bpm,8),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["la"],3,music.tempo(bpm,4),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["sol"],3,music.tempo(bpm,8),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["fa"],3,music.tempo(bpm,8),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["fa"],3,music.tempo(bpm,4),vst2,0.0,sustain)))

onda2 = np.concatenate((onda2,music.seriefourier(notas["re"],3,music.tempo(bpm,8),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["mi"],3,music.tempo(bpm,8),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["fa"],3,music.tempo(bpm,8),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["la"],3,music.tempo(bpm,4),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["sol"],3,music.tempo(bpm,4),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["fa"],3,music.tempo(bpm,4),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["do"],3,music.tempo(bpm,8),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["sol"],3,music.tempo(bpm,2),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["do"],3,music.tempo(bpm,8),vst2,0.0,sustain)))#
onda2 = np.concatenate((onda2,music.seriefourier(notas["re"],3,music.tempo(bpm,8),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["fa"],3,music.tempo(bpm,8),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["re"],3,music.tempo(bpm,8),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["sol"],3,music.tempo(bpm,3),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["la"],3,music.tempo(bpm,8),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["sol"],3,music.tempo(bpm,8),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["fa#"],3,music.tempo(bpm,3),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["re"],3,music.tempo(bpm,8),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["mi"],3,music.tempo(bpm,8),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["fa"],3,music.tempo(bpm,4),vst2,0.5,sustain)))

for _ in range(9):
    drums = np.concatenate((drums,music.drumClip(kick,music.tempo(bpm,2))))
    drums = np.concatenate((drums,music.drumClip(snare,music.tempo(bpm,2))))

bass = np.concatenate((bass,bajo_sib))
bass = np.concatenate((bass,bajo_sib))
bass = np.concatenate((bass,bajo_do))
bass = np.concatenate((bass,bajo_do))
bass = np.concatenate((bass,bajo_re))
bass = np.concatenate((bass,bajo_re))
bass = np.concatenate((bass,bajo_fa))
bass = np.concatenate((bass,bajo_fa))

bass = np.concatenate((bass,bass))
bass = np.concatenate((bass,bass))

mix = music.normalizar([onda2[i]+drums[i]+bass[i] for i in range(int(compaz*music.FM))])
mix = np.concatenate((mix,mix))

song = np.concatenate((song,mix))

"""
def aux_Arp(n1:float, o1:float, n2:float, o2:float, n3:float, o3:float, n4:float, o4:int) -> list:
    a = []
    a = np.concatenate((a,music.seriefourier(n1,o1,music.tempo(bpm,8),vst1,0.7,sustain)))
    a = np.concatenate((a,music.seriefourier(n2,o2,music.tempo(bpm,8),vst1,0.6,sustain)))
    a = np.concatenate((a,music.seriefourier(n3,o3,music.tempo(bpm,8),vst1,0.5,sustain)))
    a = np.concatenate((a,music.seriefourier(n4,o4,music.tempo(bpm,8),vst1,0.6,sustain)))
    return a

# ENDING
print("Compilando parte Final")

onda1 = []
onda2 = []
bass = []
drums = []

onda1 = np.concatenate((onda1,aux_Arp(notas["do"],3,notas["re"],3,notas["la"],2,notas["fa"],2)))
onda1 = np.concatenate((onda1,aux_Arp(notas["la"],1,notas["re"],2,notas["fa"],2,notas["fa"],3)))
onda1 = np.concatenate((onda1,aux_Arp(notas["la"],1,notas["re"],2,notas["fa"],2,notas["fa"],3)))
onda1 = np.concatenate((onda1,aux_Arp(notas["fa"],2,notas["fa"],3,notas["la"],2,notas["fa"],2)))
onda1 = np.concatenate((onda1,aux_Arp(notas["la"],1,notas["fa"],2,notas["re"],2,notas["fa"],2)))
onda1 = np.concatenate((onda1,aux_Arp(notas["la"],1,notas["fa"],2,notas["re"],2,notas["fa"],2)))
onda1 = np.concatenate((onda1,aux_Arp(notas["fa"],3,notas["sol"],3,notas["la"],2,notas["fa"],2)))
onda1 = np.concatenate((onda1,aux_Arp(notas["fa"],3,notas["sol"],3,notas["la"],2,notas["fa"],2)))
onda1 = np.concatenate((onda1,aux_Arp(notas["sol"],3,notas["la"],3,notas["fa"],3,notas["re"],3)))
onda1 = np.concatenate((onda1,aux_Arp(notas["sol"],3,notas["la"],3,notas["fa"],3,notas["re"],3)))
onda1 = np.concatenate((onda1,aux_Arp(notas["la#"],3,notas["la"],3,notas["sol"],3,notas["fa"],3)))
onda1 = np.concatenate((onda1,aux_Arp(notas["la#"],3,notas["la"],3,notas["sol"],3,notas["fa"],3)))
onda1 = np.concatenate((onda1,aux_Arp(notas["la#"],3,notas["la"],3,notas["sol"],3,notas["fa"],3)))
onda1 = np.concatenate((onda1,aux_Arp(notas["la#"],3,notas["la"],3,notas["sol"],3,notas["fa"],3)))
onda1 = np.concatenate((onda1,aux_Arp(notas["do"],2,notas["mi"],2,notas["sol"],2,notas["do"],3)))
onda1 = np.concatenate((onda1,aux_Arp(notas["re"],2,notas["fa"],2,notas["la"],2,notas["re"],3)))
onda1 = np.concatenate((onda1,aux_Arp(notas["re"],2,notas["fa"],2,notas["la"],2,notas["re"],3)))
onda1 = np.concatenate((onda1,aux_Arp(notas["la"],1,notas["mi"],2,notas["sol"],2,notas["do"],3)))
onda1 = np.concatenate((onda1,aux_Arp(notas["do"],2,notas["mi"],2,notas["sol"],2,notas["do"],3)))

onda2 = np.concatenate((onda2,music.seriefourier(notas["la"],3,music.tempo(bpm,2),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["mi"],3,music.tempo(bpm,4),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["la"],3,music.tempo(bpm,4),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["mi"],3,music.tempo(bpm,5),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["fa"],3,music.tempo(bpm,9),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["mi"],3,music.tempo(bpm,9),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["re"],3,music.tempo(bpm,5),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["re"],3,music.tempo(bpm,4),vst2,0.0,sustain)))#
onda2 = np.concatenate((onda2,music.seriefourier(notas["mi"],3,music.tempo(bpm,9),vst2,0.0,sustain)))#
onda2 = np.concatenate((onda2,music.seriefourier(notas["mi"],3,music.tempo(bpm,9),vst2,0.0,sustain)))#

onda2 = np.concatenate((onda2,music.seriefourier(notas["la"],3,music.tempo(bpm,4),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["fa"],3,music.tempo(bpm,4),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["re"],3,music.tempo(bpm,4),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["la"],3,music.tempo(bpm,4),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["la"],3,music.tempo(bpm,4),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["sol"],3,music.tempo(bpm,4),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["fa"],3,music.tempo(bpm,4),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["do"],4,music.tempo(bpm,1),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["fa"],3,music.tempo(bpm,2),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["do"],4,music.tempo(bpm,2),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["sol"],3,music.tempo(bpm,0),vst2,0.5,sustain)))
onda2 = np.concatenate((onda2,music.seriefourier(notas["sol"],3,music.tempo(bpm,0),vst2,0.5,sustain)))

for _ in range(8):
    bass = np.concatenate((bass,bajo_re))
bass = np.concatenate((bass,bajo_sib))
bass = np.concatenate((bass,bajo_sib))
bass = np.concatenate((bass,bajo_do))
for _ in range(4):
    bass = np.concatenate((bass,bajo_la))
bass = np.concatenate((bass,bajo_la))
bass = np.concatenate((bass,bajo_la))

for _ in range(9):
    drums = np.concatenate((drums,music.drumClip(kick,music.tempo(bpm,2))))
    drums = np.concatenate((drums,music.drumClip(snare,music.tempo(bpm,2))))

ondaAux = music.normalizar([onda1[i]+onda2[i] for i in range(int(compaz*music.FM))])
mix = music.normalizar([bass[i]+drums[i]+ondaAux for i in range(int(compaz*music.FM))])

music.renderAudio(mix,"canción_3_A")