#########################################################
### Archivo de prueba para aprender sobre los strings ###
#########################################################

# Almaceno en un string en una variable
myStr = "Hello world"

# Muestro en pantalla un string
print("Their first words were " + myStr) # Concatenados
print(f"Their first words were {myStr}") # Con la "f" interpreta la variable entre llaves
print("Their first words were {0}".format(myStr)) # Forma rara
print("Their first words were", myStr) # Forma cuca

# dir(var) -> Función que muestra en pantalla las posibles propiedades y métodos para mi string
# print(dir(myStr))

# len(var) -> Función que da la longitud de un string (desde el 0)
print(len(myStr))

# .upper() -> Método que transforma a mayúsculas
print(myStr.upper())

# .lower() -> Método que transforma a minúsculas
print(myStr.lower())

# .swapcase() -> Método que intercambia máyus y minus
print(myStr.swapcase())

# .capitalize() -> Método que pone la primera en mayúscula
print(myStr.capitalize())

# .replace("to_remove", "to_add") -> Método que reemplaza una parte del string
print(myStr.replace("Hello", "Bye"))
print(myStr.replace("Hello", "Bye").upper()) # Métodos encadenados

# .count("to_count") -> Método que cuenta las apariciones de un string dentro de otro
print(myStr.count("l"))

# .startswith("to_search") -> Método que comprueba si empieza por un string
print(myStr.startswith("hel"))

# .endswith("to_search") -> Método que comprueba si termina por un string
print(myStr.endswith("d"))

# .split() -> Método que separa un string en una lista
print(myStr.split()) # Separa por espacio
print(myStr.split(",")) # Separa por coma
print(myStr.split("o")) # Separa por "o"

# .find("to_find") -> Método que da la posición numérica (desde el 0) de un string
print(myStr.find("o"))

# .index("to_index") -> Método que da la posición numérica (desde el 0) de un string
print(myStr.index("Hello")) 

# .isnumeric() -> Método que comprueba si es numérico
print(myStr.isnumeric()) 

# .isalpha() -> Método que comprueba si es alfanumérico (letras y números)
print(myStr.isalpha()) 

# var[n] -> Propiedad que ofrece el enésimo caracter del string (desde el 0)
print(myStr[4])
print(myStr[-1]) # Último elemento

