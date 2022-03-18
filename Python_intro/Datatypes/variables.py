########################################################################
### Archivo de prueba para aprender los distintos tipos de variables ###
########################################################################

# Las variables almacenan un valor (de cualquier tipo) con un nombre clave
name = "Luis"
print(name)

# Python es un lenguaje de tipado dinámico. El tipo que almacena una variable
# puede ser reasignado sin mayor especificación

abc = 1
abc = (a, b, c)
abc = "Peter"
abc = False

# Las variables son "case sensitive"
book = "El camino de los reyes"
Book = "El camino de los reyes"

# No es válido empezar una variable con un número, pero sí con un guión, por ejemplo
#3book
-book = "El camino de los reyes"

# Se puede asignar valor a las variables separando mediante comas
# También mostrarlas por pantalla de esa forma (en línea)
x, y, z = 1, "Pepe", True
print(x, y, z)

# Por convención, las variables constantes se escriben en mayúscula

PI = 3.1416