## Plantilla para Decorar los Plots de Matplotlib

import matplotlib.pyplot as plt

x = [i-10 for i in range(30)]
y = [i**2 for i in x]


plt.plot(x,y) 
plt.show()