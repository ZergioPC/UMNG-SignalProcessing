""" TRABAJO EXTRACLASE SEMANA 1 - Sergio Palacios"""
# Imports
import numpy as np
import matplotlib.pyplot as plt

# 3. Desarrolle un código en Python que permita convertir un valor dado a dBFS, use como referencia 16 bits
def toDBFS(A):
    return 10*np.log10(A/32767)

def ejercicio3():
    amplitud = input("ingrese la amplitud: ")
    amplitud = int(amplitud)
    
    while amplitud > (2**15-1):
        print("Error: La amplitud no puede superar los 16bits de profundidad (32.767)\n")
        amplitud = input("ingrese la amplitud: ")
        amplitud = int(amplitud)
    
    print(toDBFS("Su amplitud en dBFS equivale a: "+amplitud))

# 4. Desarrolle un código que Genere una señal seno de 100Hz con un valor pico de -3dBFS
def ondaSeno(Fm,w,T,a=1,phi=0):
    s = []
    for t in range(Fm*T):
        s.append((a*np.sin((2*np.pi/Fm)*w*t))+phi)   
    return np.array(s)

def ejercicio4():
    """
    -3 = 10*np.log(A/(2**15-1))
    10**(-3/10) = A/(2**15-1)
    A = (2**15-1)/10**(3/10)
    A = 16442.40208...
    """
    frequencia = 100
    rta = (2**15-1)/10**(3/10)
    
    onda = ondaSeno(44100,frequencia,1,a=rta)

    plt.text(400,0,"debemos usar una amplitud de 16442.40208",ha='right',wrap=True,fontsize=10,backgroundcolor="#fff20030",color="#000000aa")
    plt.text(0,-10000,f"{rta} = {np.round(toDBFS(rta),decimals=3)} dBFS",ha='left',wrap=True,fontsize=10,backgroundcolor="#fffff030",color="#000000aa")
    plt.plot([i for i in range(len(onda[:441]))],onda[:441])
    plt.show()

# 5. Desarrolle un código que Genere una señal cuadrada de 250Hz con un valor pico de -6dBFS
def ondaCuadrada(Fm,w,T,a=1,phi=0):
    s = []
    for t in range(Fm*T):
        if (a*np.sin((2*np.pi/Fm)*w*t)+phi < 0):
            s.append(-1 * a)
        else:
            s.append(1 * a)
    return np.array(s)

def ejercicio5():
    """
    -6 = 10*np.log(A/(2**15-1))
    10**(-6/10) = A/(2**15-1)
    A = (2**15-1)/10**(6/10)
    A = 8230.6982...
    """
    frequencia = 250
    rta = (2**15-1)/10**(6/10) 
    
    onda = ondaCuadrada(44100,frequencia,1,a=rta)

    plt.text(400,0,"debemos usar una amplitud de 8230.6982",ha='right',wrap=True,fontsize=10,backgroundcolor="#fff20030",color="#000000aa")
    plt.text(0,-5000,f"{rta} = {np.round(toDBFS(rta),decimals=3)} dBFS",ha='left',wrap=True,fontsize=10,backgroundcolor="#fffff030",color="#000000aa")
    plt.plot([i for i in range(len(onda[:441]))],onda[:441])
    plt.show()


#ejercicio3()
#ejercicio4()
ejercicio5()