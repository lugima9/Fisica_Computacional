# Programa que simula la dinámica del péndulo real
# Autor: Luis Gil Martín
# Universidad de Granada

import math as math
import numpy as np
import matplotlib.pyplot as plt

PI = 4.*math.atan(1) #Defino PI


#Especificamos las propiedades del péndulo
g = 9.8     #Aceleración de la gravedad de 9.8 m/s^2

#Especificamos el paso temporal a utilizar
h = 0.1

#Especificamos las condiciones iniciales
t_0 = .0
ang_0 = 0.25*PI
vAng_0 = .0

#Definimos el algoritmo de Verlet para el péndulo.
#Devuelve una tupla con la lista de tiempo, posiciones y velocidades

def VerletPendulo(g, t_0, h, ang_0, vAng_0):
    #Valores iniciales de las listas
    t, ang, vAng, aAng, w = []*101, []*101, []*101, []*101, []*101

    t.insert(0, t_0)
    ang.insert(0, ang_0)
    vAng.insert(0, vAng_0)
    aAng.insert(0, -g*math.sin(ang_0))
    for i in range(0, 100, 1):
        t.insert(i+1, t[i] + h)
        w.insert(i, vAng[i] + 0.5*h*aAng[i])
        ang.insert(i+1, ang[i] + h*w[i])
        aAng.insert(i+1, -g*math.sin(ang[i+1]))
        vAng.insert(i+1, w[i] + 0.5*h*aAng[i+1])

    return (t, ang, vAng)

resultados = VerletPendulo(g, t_0, h, ang_0, vAng_0)    #Tupla de resultados

#Plotteamos el resultado en pantalla

fig, ax = plt.subplots()

ax.plot(resultados[0], resultados[1], linewidth=2.0)

plt.show()