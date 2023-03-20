import numpy as np
import matplotlib.pyplot as plt
import math


A = 230 * np.sqrt(2)
f = 50
omega = 2 * np.pi * f
phi = 0

#x(t) = A * np.cos(omega * czas + phi) --- wzor funkcji


T = 0.2
fs = 1000
dt = 1/fs

czas = np.arange(0, T, dt) #wektor czasu
print(czas)

x = A * np.cos(omega * czas + phi)
print(x)

plt.plot(czas, x)
plt.grid()
plt.show()

#   WIDMO

#   DFT

def iexp(n):
    return complex(math.cos(n), math.sin(n))

N = T/dt
x=A*np.cos(omega*czas+phi)

X=np.zeros(np.size(x))
X1 = np.zeros(np.size(x))

for k in range(0, int(N)):
     for n in range(0, int(N)):
         X[k] = X[k] + (x[n] * iexp((-2 * np.pi / N) * k * n))

#plots
plt.stem(2*np.abs(X)/N)
plt.grid()
plt.title("Widmo (DFT)")
plt.show()


# IDFT
for n in range(0,int(N)):
    for k in range(0,int(N)):
        X1[n]=X1[n]+(1/N)*(X[k]*iexp((2*np.pi/N)*k*n))

#plots
plt.plot(X1)
plt.plot(x)
plt.title("IDFT")
plt.show()

plt.plot(X1-x)  #porównanie
plt.title("Porównanie")
plt.show()


#  wewnętrzne funkcje FFT

fft = np.fft.fft(x)
plt.plot(czas, fft)
plt.plot(czas, fft, 'r*')
plt.show()


# wewnętrzne funkcje IFFT

ifft = np.fft.ifft(fft)
plt.plot(czas, ifft, 'g')
plt.plot(czas, x, '-b')
plt.plot(czas, x-ifft) #
plt.show()


#Widmo funkcji łączonej
zera = np.zeros(5000*9)
fft = np.fft.fft(np.append(x, zera))
ifft = np.fft.ifft(fft)

plt.plot(czas, ifft)
plt.show()