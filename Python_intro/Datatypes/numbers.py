#########################################################
### Archivo de prueba para aprender sobre los números ###
#########################################################

## OPERADORES ##
# Siguen el mismo orden de prioridad de las operaciones
# matemáticas usuales. Los paréntesis imponen jerarquía.

# x + y -> Ofrece la suma de dos números.
# Si ambos son int, resulta int
# Si al menos uno es float, resulta float

print(3+1, 2+2.0, 3.3+3.3)

# x - y -> Ofrece la resta de dos números.
# Si ambos son int, resulta int
# Si al menos uno es float, resulta float

print(3-1, 2-2.0, 3.3-3.3)

# x * y -> Ofrece el producto de dos números.
# Si ambos son int, resulta int
# Si al menos uno es float, resulta float

print(3*1, 2*2.0, 3.3*3.3)

# x / y -> Ofrece el cociente de dos números.

print(3/2, 2/2.0, 3.3/4.87)

# x ** y -> Ofrece la y-ésima potencia de x.

print(3**1, 2**2.0, 3.3**3.3)

# x // y -> Ofrece la división entera de dos enteros.

print(3//1, 2//3, 7//2)

# x % y -> Ofrece el módulo (resto) del cpciente de dos enteros.

print(3%1, 2%2, 7%3)

## INTERACCIÓN CON EL USUARIO ##

# Ejemplo: Programa que calcula los años que quedan para ser mayor de edad
age = input("Insert your age (below 18): ") # Toma la edad como string
years_left = 18 - int(age) # Convierte el input en int
print("You will be 18 in", years_left, "years.")

