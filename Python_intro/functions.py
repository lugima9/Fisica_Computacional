###########################################################
### Archivo de prueba para aprender sobre las funciones ###
###########################################################

# Una función es una porción de código ya escrito al que se
# se le pasa un dato y ofrece otro.

# Ejemplo: Función que dice "Hello, name"

def hello(name="MISSING_NAME"): # Defino la función con un parám. por defecto
    print("Hello,", name)

hello("Pepe Luis")              # Llamo a la función

# Ejemplo: Función que suma número complejos

def c_sum_1(c1, c2): #Toma tuplas como argumentos
    return (c1[0]+c2[0], c1[1]+c2[1])

print(c_sum_1((1,2), (3, 7)))

# MÉTODO ALTERNATIVO CON LAMBDA (Función anónima simple)

c_sum_2 = lambda c1, c2: (c1[0]+c2[0], c1[1]+c2[1])

print(c_sum_2((1,2), (3, 7)))

