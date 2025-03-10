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
    def __init__(self,onda1,freq1,onda2,freq2,amplitud,punto):
        self.onda1 = onda1
        self.onda2 = onda2
        self.freq1 = freq1
        self.freq2 = freq2
        self.a = amplitud
        self.T1 = int(44100/freq1)
        self.T2 = int(44100/freq2)
        self.titulo = ''
        self.punto = punto

    def renderAudio(self,onda,name):
        onda_16bits = (np.array(onda)*32767).astype(np.int16)
        wavfile.write(f'./audios/taller_02/{self.punto}/{name}.wav',44100,onda_16bits)

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
        self.renderAudio(rta,'a_X[n] y Y[n]')
    
    def punto2(self):
        x = self.onda1(self.freq1,self.a)
        y = self.onda2(self.freq2,self.a)

        rta = (x + y)
        rta = [-i for i in rta]
        
        tiempo = np.linspace(0,6,len(rta))
        self.graficar('X[-n] y Y[-n]',tiempo,rta)
        self.renderAudio(rta,'b_X[-n] y Y[-n]')
    
    def punto3(self):
        x = self.onda1(self.freq1,self.a)
        x = [x[2*n] for n in range(int(len(x)/2))]

        y = self.onda2(self.freq2,self.a)
        y = [y[2*n] for n in range(int(len(y)/2))]

        rta = (x + y)
        
        tiempo = np.linspace(0,3,len(rta))
        self.graficar('X[2n] y Y[2n]',tiempo,rta)
        self.renderAudio(rta,'c_X[2n] y Y[2n]')

    def punto4(self):
        x = self.onda1(self.freq1,self.a)
        x = [x[3*n] for n in range(int(len(x)/3))]

        y = self.onda2(self.freq2,self.a)
        y = [y[3*n] for n in range(int(len(y)/3))]

        rta = (x + y)
        
        tiempo = np.linspace(0,2,len(rta))
        self.graficar('X[3n] y Y[3n]',tiempo,rta)
        self.renderAudio(rta,'d_X[3n] y Y[3n]')        

    def punto5(self):
        x = self.onda1(self.freq1,self.a)
        x = [x[int(n/2)] for n in range(int(len(x)*2))]

        y = self.onda2(self.freq2,self.a)
        y = [y[int(n/2)] for n in range(int(len(y)*2))]

        rta = (x + y)
        
        tiempo = np.linspace(0,12,len(rta))
        self.graficar('X['+r'$\frac{n}{2}$'+'] y Y['+r'$\frac{n}{2}$'+']',tiempo,rta)
        self.renderAudio(rta,'e_X[n÷2] y Y[n÷2]')
    
    def punto6(self):
        x = self.onda1(self.freq1,self.a)
        y = self.onda2(self.freq2,self.a)
        
        size = menorList([x,y])
        rta = [(x[n]+y[n]) for n in range(size)]

        tiempo = np.linspace(0,3,len(rta))
        self.graficar('X[n] + Y[n]',tiempo,rta)
        self.renderAudio(rta,'f_X[n] + Y[n]')

    def punto7(self):
        x = self.onda1(self.freq1,self.a)
        x2 = [x[2*n] for n in range(int(len(x)/2))]
        x3 = [x[3*n] for n in range(int(len(x)/3))]

        for n in range(len(x)-len(x2)):
            x2.append(0)
        
        for n in range(len(x)-len(x3)):
            x3.append(0)

        size = menorList([x,x2,x3])
        rta = [(x[n]+x2[n]+x3[n]) for n in range(size)]

        tiempo = np.linspace(0,5.5,len(rta))
        self.graficar('X[n] + X[2n] + X[3n]',tiempo,rta)
        self.renderAudio(rta,'g_X[n] + X[2n] + X[3n]')

    def punto8(self):
        x = self.onda1(self.freq1,self.a)
        y = self.onda2(self.freq2,self.a)
        
        rta = ([0.5*n for n in x] + [0.5*n for n in y])

        tiempo = np.linspace(0,6,len(rta))
        self.graficar('0.5 X[n] y 0.5 Y[n]',tiempo,rta)
        self.renderAudio(rta,'h_0.5·X[n] y 0.5·Y[n]')
    
    def punto9(self):
        x = self.onda1(self.freq1,self.a)
        y = self.onda2(self.freq2,self.a)
        z1 = int(self.T1/4)
        z2 = int(self.T2/4)
        
        rta = (x[z1:] + y[z2:])

        tiempo = np.linspace(0,3,len(rta))
        self.graficar('X[n-z] y Y[n-z]',tiempo,rta)
        self.renderAudio(rta,'i_X[n-z] y Y[n-z]')

    def punto10(self):
        x = self.onda1(self.freq1,self.a)
        y = self.onda2(self.freq2,self.a)
        
        z1 = int(self.T1/4)
        x = x[z1:]

        for n in range(len(y)-len(x)):
            x.append(0)

        size = menorList([x,y])
        rta = [y[n]+x[n] for n in range(size)]

        tiempo = np.linspace(0,3,len(rta))
        self.graficar('Y[n] + X[n-z]',tiempo,rta)
        self.renderAudio(rta,'j_Y[n] + X[n-z]')
    
    def punto11(self):
        x = self.onda1(self.freq1,self.a)
        y = self.onda2(self.freq2,self.a)
        
        x1 = [n*0.5 for n in x]
        y = [y[n*2]*0.3 for n in range(int(len(y)/2))]
        x2 = [x[n*3]*0.2 for n in range(int(len(x)/3))]

        for n in range(len(x)-len(y)):
            y.append(0)
        
        for n in range(len(x)-len(x2)):
            x2.append(0)

        size = menorList([x1,y,x2])
        rta = [x1[n]+y[n]+x2[n] for n in range(size)]

        tiempo = np.linspace(0,3,len(rta))
        self.graficar('0.5 X[n] + 0.3 Y[2n] + 0.2 X[3n]',tiempo,rta)
        self.renderAudio(rta,'k_0.5·X[n] + 0.3·Y[2n] + 0.2·X[3n]')

    def punto12(self):
        x = self.onda1(self.freq1,self.a)
        y = self.onda2(self.freq2,self.a)
        w = int(self.T1/8)
        z = int(self.T2/4)
        
        x1 = [n*0.5 for n in x[w:]]
        y = [y[2*n]*0.3 for n in range(int(len(y[z:])/2))]
        x2 = [x[3*n]*0.2 for n in range(int(len(x)/3))]

        for n in range(len(x)-len(x1)):
            x1.append(0)
        
        for n in range(len(x)-len(y)):
            y.append(0)

        for n in range(len(x)-len(x2)):
            x2.append(0)

        size = menorList([x1,y,x2])
        rta = [(x1[n]+y[n]+x2[n]) for n in range(size)]

        tiempo = np.linspace(0,3,len(rta))
        self.graficar('0.5 X[n-w] + 0.3 Y[2n-z] + 0.2 X[3n]',tiempo,rta)
        self.renderAudio(rta,'l_0.5·X[n-w] + 0.3·Y[2n-z] + 0.2·X[3n]')

    def resolver(self):
        self.punto1()
        self.punto2()
        self.punto3()
        self.punto4()
        self.punto5()
        self.punto6()
        self.punto7()
        self.punto8()
        self.punto9()
        self.punto10()
        self.punto11()
        self.punto12()


# RESPUESTAS #

amplitud = DBtoBYTE(-6)

""" 1. X[n] = señal seno a 500Hz, y[n] = señal diente de sierra a 750Hz """

primero = ejercicios(ondaSeno,500,ondaSierra,750,amplitud,"1")
primero.titulo = 'Señal seno a 500Hz y señal diente de sierra a 750Hz'
primero.resolver()

""" 2. X[n] = señal cuadrada a 600Hz, y[n] = señal diente de sierra a 900Hz """

segundo = ejercicios(ondaCuadrada,600,ondaSierra,900,amplitud,"2")
segundo.titulo = 'Señal cuadrada a 600Hz y señal diente de sierra a 900Hz'
segundo.resolver()

""" 3. X[n] = señal triangular a 600Hz, y[n] = señal diente de sierra a 900Hz """

tercero = ejercicios(ondaTriangulo,600,ondaSierra,900,amplitud,"3")
tercero.titulo = 'Señal triangulo a 600Hz y señal diente de sierra a 900Hz'
tercero.resolver()

""" 4.X[n] = señal diente de sierra a 800Hz, y[n] = señal cuadrada a 400Hz  """

cuarto = ejercicios(ondaSierra,800,ondaCuadrada,400,amplitud,"4")
cuarto.titulo = 'Señal sierra a 800Hz y señal diente de cuadrado a 400Hz'
cuarto.resolver()

""" 5. X[n] = señal triangular a 1000Hz, y[n] = señal seno a 500Hz """

quinto = ejercicios(ondaTriangulo,1000,ondaSeno,500,amplitud,"5")
quinto.titulo = 'Señal sierra a 800Hz y señal diente de cuadrado a 400Hz'
quinto.resolver()