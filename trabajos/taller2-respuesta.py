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

    def punto1(self):
        x = self.onda1(self.freq1,self.a)
        y = self.onda2(self.freq2,self.a)

        rta = (x + y)
        tiempo = np.linspace(0,3,len(rta))

        plt.plot(tiempo,rta)
        plt.show()
    
    def punto2(self):
        x = self.onda1(self.freq1,self.a)
        y = self.onda2(self.freq2,self.a)

        rta = (x + y)
        
        tiempo = np.linspace(0,3,len(rta))
        plt.plot(tiempo,[-i for i in rta])
        plt.show()
    
    def punto3(self):
        x = self.onda1(self.freq1,self.a)
        x = [x[n] for n in range(len(x)) if(n%2==0)]

        y = self.onda2(self.freq2,self.a)
        y = [y[n] for n in range(len(y)) if(n%2==0)]

        rta = (x + y)
        
        tiempo = np.linspace(0,3,len(rta))
        plt.plot(tiempo,rta)
        plt.show()

    def punto4(self):
        x = self.onda1(self.freq1,self.a)
        x = [x[n] for n in range(len(x)) if(n%3==0)]

        y = self.onda2(self.freq2,self.a)
        y = [y[n] for n in range(len(y)) if(n%3==0)]

        rta = (x + y)
        
        tiempo = np.linspace(0,3,len(rta))
        plt.plot(tiempo,rta)
        plt.show()

    def punto5(self):
        x = self.onda1(self.freq1,self.a)
        y = self.onda2(self.freq2,self.a)

        rta = (x + y)
        
        tiempo = np.linspace(0,3,len(rta))
        plt.plot(tiempo,[i/2 for i in rta])
        plt.show()
    
    def punto6(self):
        x = self.onda1(self.freq1,self.a)
        y = self.onda2(self.freq2,self.a)
        
        size = len(x)
        if(size > len(y)):
            size = len(y)

        rta = [(x[n]+y[n]) for n in range(size)]

        tiempo = np.linspace(0,3,len(rta))
        plt.plot(tiempo,rta)
        plt.show()

    def punto7(self):
        x = self.onda1(self.freq1,self.a)
        
        rta = (x + [x[n] for n in range(len(x)) if(n%2==0)] + [x[n] for n in range(len(x)) if(n%3==0)])

        tiempo = np.linspace(0,3,len(rta))
        plt.plot(tiempo,rta)
        plt.show()

    def punto8(self):
        x = self.onda1(self.freq1,self.a)
        y = self.onda2(self.freq2,self.a)
        
        rta = ([0.5*n for n in x] + [0.5*n for n in y])

        tiempo = np.linspace(0,3,len(rta))
        plt.plot(tiempo,rta)
        plt.show()
    
    def punto9(self):
        x = self.onda1(self.freq1,self.a)
        y = self.onda2(self.freq2,self.a)
        z1 = int(self.T1/4)
        z2 = int(self.T2/4)
        
        rta = (x[z1:] + y[z2:])

        tiempo = np.linspace(0,3,len(rta))
        plt.plot(tiempo,rta)
        plt.show()

    def punto10(self):
        x = self.onda1(self.freq1,self.a)
        y = self.onda2(self.freq2,self.a)
        
        z1 = int(self.T2/4)
        x = x[z1:]

        size = len(x)
        if(size > len(y)):
            size = len(y)

        rta = [y[n]+x[n] for n in range(size)]

        tiempo = np.linspace(0,3,len(rta))
        plt.plot(tiempo,rta)
        plt.show()
    
    def punto11(self):
        x = self.onda1(self.freq1,self.a)
        y = self.onda2(self.freq2,self.a)
        
        x1 = [n*0.5 for n in x]
        y = [y[n*2]*0.3 for n in range(int(len(y)/2))]
        x2 = [x[n*3]*0.2 for n in range(int(len(x)/3))]

        size = len(x1)
        if(size > len(y)):
            size = len(y)
        if(size > len(x2)):
            size = len(x2)

        rta = [x1[n]+y[n]+x2[n] for n in range(size)]

        tiempo = np.linspace(0,3,len(rta))
        plt.plot(tiempo,rta)
        plt.show()

    def punto12(self):
        x = self.onda1(self.freq1,self.a)
        y = self.onda2(self.freq2,self.a)
        w = int(self.T1/8)
        z = int(self.T2/4)
        
        x1 = [n*0.5 for n in x[w:]]
        y = [y[2*n-z]*0.3 for n in range(int(len(y[z:])/2))]
        x2 = [x[3*n]*0.2 for n in range(int(len(x)/3))]
        
        size = len(x1)
        if(size > len(y)):
            size = len(y)
        if(size > len(x2)):
            size = len(x2)

        rta = [(x1[n]+y[n]+x2[n]) for n in range(size)]

        tiempo = np.linspace(0,3,len(rta))
        plt.plot(tiempo,rta)
        plt.show()

# RESPUESTAS #

amplitud = DBtoBYTE(-6)

#test = ondaSeno(400,1,amplitud)
#plt.plot([i for i in range(len(test))],[-i for i in test])
#plt.show()

""" 1. X[n] = señal seno a 500Hz, y[n] = señal diente de sierra a 750Hz """

primero = ejercicios(ondaSeno,500,ondaSierra,750,amplitud)
primero.punto1()
primero.punto2()
primero.punto3()
primero.punto4()
primero.punto5()
primero.punto6()
primero.punto7()
primero.punto8()
primero.punto9()
primero.punto10()
primero.punto11()
primero.punto12()