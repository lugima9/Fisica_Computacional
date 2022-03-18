##############################################################
### Archivo de prueba para aprender sobre los diccionarios ###
##############################################################

product = {
    "prod_name": "El camino de los reyes",
    "quantity": 3,
    "price": 34.99
}

user = {
    "name": "Juan"
    "phone": 691919191
}

# .keys() -> Método que da una lista con las claves de un diccionario
product.keys() # ["prod_name", "quantity", "price"]

# .items() -> Método que da una lista con las claves e items de un diccionario
product.items() # [("prod_name", "El camino de los reyes"), ..., ...]

# .clear() -> Método que vacía el diccionario
product.clear()

# del__ -> Elimina el diccionario