## Plantilla para Decorar los Plots de Matplotlib

import matplotlib.pyplot as plt

x = [i-10 for i in range(30)]
y = [i**2 for i in x]

""" PLOT con 2 Dimensiones CARTESIANAS """

plt.figure(
    facecolor=('#c39cff'),  #Color de fondo
    edgecolor=('#523b5e'),  #Color del Borde  
    ) 
plt.title('titulo')
plt.xlabel('titulo X',loc='left')       #titulo en X
plt.ylabel('titulo Y',loc='bottom')     #titulo en Y
plt.plot(x,y) 
plt.show()