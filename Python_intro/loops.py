#######################################################
### Archivo de prueba para aprender sobre los loops ###
#######################################################

## Bucles for ##

# break -> Para el bucle for
# continue -> Continía con el siguiente loop

# Ejemplo: Programa que determina si hay que comprar pan

foods = ["milk", "bread", "grapes", "fish"]

for food in foods:
    if food == "bread":
        print("You have to buy", food)
        break # Se para el bucle si se encuentra

# Ejemplo: Programa que ignora las uvas en la lista de la compra

print("You have to buy:")
for food in foods:
    if food == "grapes":
        continue # Se salta al siguiente loop
    print(food)

# Ejemplo: Programa que imprime los números pares en un rango dado

bottom = int(input("Lowest number in the range: "))
top = int(input("Highest number in the range: ")) + 1

for number in range(bottom, top):
    if number % 2 == 0:
        print(number)

# Ejemplo: Programa que elimina las vocales de una palabra
# y las cambia por su número correspondiente con loops

vowels = ("a", "e", "i", "o", "u")

word = input("Write a word: ")

for letter in word:
    if letter.lower() in vowels:
        word=word.replace(letter, str(vowels.index(letter.lower())+1))
    
print("The word with indexed vowels is: ", word)

## Bucles while ##

# Ejemplo:

count = 4

while count <= 10:
    print(count)
    count += 1 # Incremento en 1 (count = count + 1)









    