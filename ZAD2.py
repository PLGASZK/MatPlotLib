import numpy as np
import matplotlib.pyplot as plt
E1 = 4273 # uV
E2 = 806 # uV
Tn = [12.8, 25.2, 37.3, 49.2, 60.7, 72.1, 83.2, 94.0, 104.7, 115.3, 125.6, 135.9, 146.0, 155.9, 165.6, 175.5, 185.1, 194.6, 204.0, 213.3, 222.6, 231.7, 240.8, 249.8, 258.7, 267.6, 276.4, 285.1, 293.8, 302.4, 311.0, 319.5, 328.0, 336.4, 344.7, 353.0, 361.3,  369.6, 377.7, 385.9, 394.0]
En = np.arange(start = 0, stop = 20500, step = 500)
plt.title('Charakterystyka termopary typu T (Cu-CuNi)')
plt.xlabel(' siła termoelektryczna [$\mu$V] ')
plt.ylabel('temperatura w [°C]')
plt.plot(En, Tn,"--b")

plt.plot(En, Tn,"*r")
plt.gca().legend(('y0','y1'))
plt.show()



##41 pkt


p = np.polyfit(En,Tn, 40)
print(p)
E_cont = np.arange(start = 0, stop = 20500, step = 5)
y = np. polyval(p, E_cont)
plt.title('Charakterystyka termopary typu T (Cu-CuNi)')
plt.xlabel(' siła termoelektryczna [$\mu$V] ')
plt.ylabel('temperatura w [°C]')
plt.plot(E_cont, y, "--b")

plt.plot(En, Tn, "*r")
plt.gca().legend(('y0','y1'))
plt.show()


E100 = 4273 # uV fpr about 100 degrees Celsius
E20 = 806 #uV for about 20 degrees Celsius

print(np.polyval(p,E100))
print(np.polyval(p,E20))


