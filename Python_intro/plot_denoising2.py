# Programa que elimina el ruido tipo "salt and pepper" de una imagen mediante filtro de mediana
# Autores/as: GET 20
# Universidad de Granada

import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
from PIL import Image

# Abrimos la imagen con ruido
im_ruido = Image.open("saltandpepper.jpg")

# Pedimos un nivel de exigencia al filtrado
exigencia = -1
while exigencia < 0:
    exigencia = int(input("¿Cuan exigente quieres el filtrado? Introduce un numero natural (Recomendacion: elige un numero entre 1 y 10): \n"))

# Aplicamos filtro de mediana a la imagen
im_filtro = ndimage.median_filter(im_ruido, size=int(exigencia))

# Mostramos el resultado
fig = plt.figure()

ax1 = fig.add_subplot(121)
ax1.set_title("Original")
ax1.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)

ax2 = fig.add_subplot(122)
ax2.set_title("Filtro mediana")
ax2.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)

ax1.imshow(im_ruido)   
ax2.imshow(im_filtro)

plt.show()

