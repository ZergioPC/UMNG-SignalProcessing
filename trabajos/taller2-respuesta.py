"""
TALLER PRÁCTICO #1 -  PROCESAMIENTO DE SEÑALES
Sergio Palacios
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# AUXILIARES

def pendiente(x0,x1,y0,y1):
    return (y1-y0)/(x1-x0)

def recta(x0,y0,m):
    return y0-(m*x0)

def DBtoBYTE(db):
    return 10**(db/10)

def menorList(listas):
    size = len(listas[0])
    for lista in listas:
        if (len(lista) < size):
            size = len(lista)
    return size

def ondaSeno(w,a,phi=0):
    Fm = 44100
    T = 3
    s = []
    for t in range(int(Fm*T)):
        aux = (a*np.sin((2*np.pi/Fm)*w*t))+phi
        s.append(aux)   
    return s

def ondaCuadrada(w,a,phi=0):
    Fm = 44100
    T = 3
    s = []
    for t in range(int(Fm*T)):
        aux = (np.sin((2*np.pi/Fm)*w*t))+phi
        if(aux < 0):
            s.append(-a)   
        else:
            s.append(a)
    return s

def ondaTriangulo(w,a,phi=0):
    Fm = 44100
    T = 3
    periodo = int(Fm/w)
    frecuencia = int(T*w)

    m1 = pendiente(0,periodo/4,0,1)
    b1 = recta(0,0,m1)
    m2 = pendiente(periodo/4,(3*periodo)/4,1,-1)
    b2 = recta(periodo/4,1,m2)
    m3 = pendiente((3*periodo)/4,periodo,-1,0)
    b3 = recta((3*periodo)/4,-1,m3)
    
    s = []

    for t in range(frecuencia):
        for x in range(periodo):
            if(x < periodo/4):
                s.append((m1*x)+b1)
            elif(x >= periodo/4 and x < 3*periodo/4):
                s.append((m2*x)+b2)
            else:
                s.append((m3*x)+b3)
    
    return [i*a for i in s]

def ondaSierra(w,a,phi=0):
    Fm = 44100
    T = 3
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

class ejercicios:
    def __init__(self,onda1,freq1,onda2,freq2,amplitud):
        self.onda1 = onda1
        self.onda2 = onda2
        self.freq1 = freq1
        self.freq2 = freq2
        self.a = amplitud
        self.T1 = int(44100/freq1)
        self.T2 = int(44100/freq2)
        self.titulo = ''

    def graficar(self,label,xData,yData):
        plt.figure(num="Taller 2 - Sergio Palacios") 
        plt.title(self.titulo)
        plt.xlabel('Tiempo')
        plt.ylabel(label)
        plt.plot(xData,yData) 
        plt.show()

    def punto1(self):
        x = self.onda1(self.freq1,self.a)
        y = self.onda2(self.freq2,self.a)

        rta = (x + y)
        tiempo = np.linspace(0,6,len(rta))
        self.graficar('X[n] y Y[n]',tiempo,rta)
    
    def punto2(self):
        x = self.onda1(self.freq1,self.a)
        y = self.onda2(self.freq2,self.a)

        rta = (x + y)
        rta = [-i for i in rta]
        
        tiempo = np.linspace(0,6,len(rta))
        self.graficar('X[-n] y Y[-n]',tiempo,rta)
    
    def punto3(self):
        x = self.onda1(self.freq1,self.a)
        x = [x[2*n] for n in range(int(len(x)/2))]

        y = self.onda2(self.freq2,self.a)
        y = [y[2*n] for n in range(int(len(y)/2))]

        rta = (x + y)
        
        tiempo = np.linspace(0,3,len(rta))
        self.graficar('X[2n] y Y[2n]',tiempo,rta)

    def punto4(self):
        x = self.onda1(self.freq1,self.a)
        x = [x[3*n] for n in range(int(len(x)/3))]

        y = self.onda2(self.freq2,self.a)
        y = [y[3*n] for n in range(int(len(y)/3))]

        rta = (x + y)
        
        tiempo = np.linspace(0,2,len(rta))
        self.graficar('X[3n] y Y[3n]',tiempo,rta)

    def punto5(self):
        x = self.onda1(self.freq1,self.a)
        x = [x[int(n/2)] for n in range(int(len(x)/2))]

        y = self.onda2(self.freq2,self.a)
        y = [y[int(n/2)] for n in range(int(len(y)/2))]

        rta = (x + y)
        
        tiempo = np.linspace(0,12,len(rta))
        self.graficar('X['+r'$\frac{n}{2}$'+'] y Y['+r'$\frac{n}{2}$'+']',tiempo,rta)
    
    def punto6(self):
        x = self.onda1(self.freq1,self.a)
        y = self.onda2(self.freq2,self.a)
        
        size = menorList([x,y])
        rta = [(x[n]+y[n]) for n in range(size)]

        tiempo = np.linspace(0,3,len(rta))
        self.graficar('X[n] + Y[n]',tiempo,rta)

    def punto7(self):
        x = self.onda1(self.freq1,self.a)
        x2 = [x[2*n] for n in range(int(len(x)/2))]
        x3 = [x[3*n] for n in range(int(len(x)/3))]

        size = menorList([x,x2,x3])
        rta = [(x[n]+x2[n]+x3[n]) for n in range(size)]

        tiempo = np.linspace(0,5.5,len(rta))
        self.graficar('X[n] + X[2n] + X[3n]',tiempo,rta)

    def punto8(self):
        x = self.onda1(self.freq1,self.a)
        y = self.onda2(self.freq2,self.a)
        
        rta = ([0.5*n for n in x] + [0.5*n for n in y])

        tiempo = np.linspace(0,6,len(rta))
        self.graficar('0.5 X[n] y 0.5 Y[n]',tiempo,rta)
    
    def punto9(self):
        x = self.onda1(self.freq1,self.a)
        y = self.onda2(self.freq2,self.a)
        z1 = int(self.T1/4)
        z2 = int(self.T2/4)
        
        rta = (x[z1:] + y[z2:])

        tiempo = np.linspace(0,3,len(rta))
        self.graficar('X[n-z] y Y[n-z]',tiempo,rta)

    def punto10(self):
        x = self.onda1(self.freq1,self.a)
        y = self.onda2(self.freq2,self.a)
        
        z1 = int(self.T1/4)
        x = x[z1:]

        size = menorList([x,y])
        rta = [y[n]+x[n] for n in range(size)]

        tiempo = np.linspace(0,3,len(rta))
        self.graficar('Y[n] + X[n-z]',tiempo,rta)
    
    def punto11(self):
        x = self.onda1(self.freq1,self.a)
        y = self.onda2(self.freq2,self.a)
        
        x1 = [n*0.5 for n in x]
        y = [y[n*2]*0.3 for n in range(int(len(y)/2))]
        x2 = [x[n*3]*0.2 for n in range(int(len(x)/3))]

        size = menorList([x1,y,x2])
        rta = [x1[n]+y[n]+x2[n] for n in range(size)]

        tiempo = np.linspace(0,3,len(rta))
        self.graficar('0.5 X[n] + 0.3 Y[2n] + 0.2 X[3n]',tiempo,rta)

    def punto12(self):
        x = self.onda1(self.freq1,self.a)
        y = self.onda2(self.freq2,self.a)
        w = int(self.T1/8)
        z = int(self.T2/4)
        
        x1 = [n*0.5 for n in x[w:]]
        y = [y[2*n]*0.3 for n in range(int(len(y[z:])/2))]
        x2 = [x[3*n]*0.2 for n in range(int(len(x)/3))]
        
        size = menorList([x1,y,x2])
        rta = [(x1[n]+y[n]+x2[n]) for n in range(size)]

        tiempo = np.linspace(0,3,len(rta))
        self.graficar('0.5 X[n-w] + 0.3 Y[2n-z] + 0.2 X[3n]',tiempo,rta)

# RESPUESTAS #

amplitud = DBtoBYTE(-6)

""" 1. X[n] = señal seno a 500Hz, y[n] = señal diente de sierra a 750Hz """

primero = ejercicios(ondaSeno,500,ondaSierra,750,amplitud)
primero.titulo = 'Señal seno a 500Hz y señal diente de sierra a 750Hz'
#primero.punto1()
#primero.punto2()
#primero.punto3()
#primero.punto4()
#primero.punto5()
#primero.punto6()
#primero.punto7()
#primero.punto8()
#primero.punto9()
#primero.punto10()
#primero.punto11()
#primero.punto12()