#########################################################
### Archivo de prueba para aprender sobre los módulos ###
#########################################################

# Módulos propios: Creados por mí

# Módulos third party: Descargados de internet
# pypi.org
# Para instalar un módulo desde internet
# > pip install module_name

# Módulos de Python: Sacados de las bibliotecas de Python
# Python module index

# Ejemplo: Importar módulo de Python que da la fecha

import datetime

print(datetime.date.today()) # Parámetro .date y método .today de datetime
print(datetime.timedelta(minutes=70)) # Método que convierte minutos en horas y minutos

# Ejemplo: Importar solo dos métodos de un módulo de Python que da la fecha

from datetime import timedelta, date

print(timedelta(minutes=70))
print(date.today())

# Ejemplo: Importar un módulo de creación propia

import mymath

print(mymath.add(3,4))

from mymath import add, substract

print(add(3,4))
print(substract(3,4))