# Programa que muestra una curva en función de un parámetro
# Autor: Luis Gil Martín
# Universidad de Granada

import math
import random
import matplotlib.pyplot as plt

PI = 4*math.atan(1)

x, y, r = [], [], []

#Se pide un valor de epsilon al usuario
eps = -1.
while eps <= 0. or eps > 1000.:
    eps = float(input("Inserte el valor de epsilon para la curva: \n"))

#Se generan los valores de la curva con una distribución uniforme de ángulos entre 0 y 2PI

for i in range(0, 10000, 1):
    ang = float(i)/(2*PI)
    r.insert(i, 1/(1+eps*math.cos(ang)))
    x.insert(i, r[i]*math.cos(ang))
    y.insert(i, r[i]*math.sin(ang))

#Plotteamos el resultado en pantalla

plt.scatter(x, y, s=0.5)

plt.show()