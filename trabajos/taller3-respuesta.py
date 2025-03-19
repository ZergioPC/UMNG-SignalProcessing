"""
TALLER PRÁCTICO #3 -  PROCESAMIENTO DE SEÑALES
Sergio Palacios
"""
import numpy as np
import matplotlib.pyplot as plt

# FUNCIÓNES AUXILIARES

def normalizar(lista):
    max = 0
    for n in lista:
        if ( np.abs(n) > max):
            max = n
    return [n for n in lista]

def convolucion(xn,hn):
    x = normalizar(xn)
    h = normalizar(hn[::-1])

    y = []

    #Convolución cuando T >= 0
    for n in range(len(h)-1):
        xAux = x[:(n+1)]    
        hAux = h[-(n+1):]  
        yAux = []           # Lista de resultado de multiplicaciones
        Aux = 0             # Sumatoria de multiplicaciones
        for i in range(len(xAux)):
            yAux.append(xAux[i]*hAux[i])
        for i in yAux:
            Aux += i
        print(f"sum: {yAux} = {Aux}")
        y.append(Aux)
    
    #Convolución intermedia
    for n in range(len(x)-len(h)):
        xAux = x[n:len(h)+n]
        yAux = []               # Lista de resultado de multiplicaciones
        Aux = 0                 # Sumatoria de multiplicaciones
        for i in range(len(xAux)):
            yAux.append(xAux[i]*h[i])
        for i in yAux:
           Aux += i
        print(f"sum: {yAux} = {Aux}")
        y.append(Aux)

    #Convolución cuando len(h)+T > len(x[n+T])
    for n in np.linspace(len(h)-1,0,len(h)):
        xAux = x[-(int(n)+1):]    
        hAux = h[:(int(n)+1)]  
        yAux = []           # Lista de resultado de multiplicaciones
        Aux = 0             # Sumatoria de multiplicaciones
        for i in range(len(xAux)):
            yAux.append(xAux[i]*hAux[i])
        for i in yAux:
            Aux += i
        print(f"sum: {yAux} = {Aux}")
        y.append(Aux)
    
    return(y)

def graficar(data,titulo,label):
    plt.figure(num="Taller #3 - Sergio Palacios")
    plt.title(titulo)
    plt.xlabel('Tiempo')
    plt.ylabel(label)
    plt.plot([n for n in range(len(data))],data) 
    plt.show()

# SOLUCIÓN

def desarrollo(x,h,num):
    print(f"Convolución X{num} y h{num}")

    print(f"\n{x}")
    print(h[::-1])
    conv1 = convolucion(x,h)
    print(conv1)
    graficar(conv1,fr"$X_{{{num}}}$"+"[n] ⁕ "fr"$h_{{{num}}}$"+"[n]","X[n] ⁕ h[n]")

    print(f"\n{x[2:]}")
    print(h[::-1])
    conv2 = convolucion(x[2:],h)
    print(conv2)
    graficar(conv1,fr"$X_{{{num}}}$"+"[n-2] ⁕ "fr"$h_{{{num}}}$"+"[n]","X[n-2] ⁕ h[n]")

    print(f"\n{([0]*5)+x}")
    print(h[::-1])
    conv3 = convolucion(([0]*5)+x,h)
    print(conv3)
    graficar(conv1,fr"$X_{{{num}}}$"+"[n+5] ⁕ "fr"$h_{{{num}}}$"+"[n]","X[n+5] ⁕ h[n]")

    print(" - * - * -")

x1 = [1,0,2,0,1,0,3,0,4,0,1,2,3,4,0]
h1 = [3,4,-1,0,1] 

x2 = [10,5,2,3,1,-6,3,-5,4,-2,1,2,3,-5,1 ]
h2 = [-1,1,-1,0,1]

x3 = [1,-1,1,-1,0,-1,0,-1,2,-2,-1,1,-2,-1,1 ] 
h3 = [-1,0,1,0,-1] 

print(" - * - * -")
desarrollo(x1,h1,1)
desarrollo(x2,h2,2)
desarrollo(x3,h3,3)