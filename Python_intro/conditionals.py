###############################################################
### Archivo de prueba para aprender sobre los condicionales ###
###############################################################

# __>__ | __<__ | __==__ -> Operaciones de comparación numérica
# __>=__ | __<=__ | __!=__
3 > 2 # True
3 < 2 # False
3 == 2 # False

# __and__ | __or__ | not__ -> Operadores lógicos

# Condicionales if:, elif:, else:
# Se pueden anidar con tabuladores

#Ejemplo: Programa que comprueba si eres mayor de edad

age = input("What is your age? ")

age = int(age)

if age < 18:
    print("You are not an adult.")
else:
    print("You are an adult")

#Ejemplo: Programa que comprueba si eres chulo

smokes = input("Do you smoke (YES/NO)? ")

smokes=smokes.upper() # Lo fijamos a máyus para ahorrar comprobaciones

if smokes == "YES":
    print("You are cool.")
elif smokes == "NO":
    print("You ain't cool")
else:
    print("Not only are you not cool, but also dumb.")
