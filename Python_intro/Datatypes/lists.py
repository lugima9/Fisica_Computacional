########################################################
### Archivo de prueba para aprender sobre las listas ###
########################################################

demo_list = [1, "hello", 1.34, True, [1,2,3]]

# list() -> Función que construye una lista a partir de un tupla
numbers_list = list((1,2,3,4))

# range() -> Función que devuelve una tupla con elementos en un rango
r = list(range(1, 101)) #Números del 1 al 100

# len() -> Función que devuelve el número de elementos de una lista
len(demo_list) #Números del 1 al 100

# var[n] -> Elemento n-ésimo de una lista (desde el 0)
demo_list[3]
demo_list[-1]
demo_list[1] = "bye" # Cambia el elemento 1.34

# __ in __ -> Comprueba si existe un elemento en una lista
"hello" in demo_list
"bye" in demo_list

# .index(element) -> Método que ofrece el índice de un elemento buscado
demo_list.index(1)

# .count(element) -> Método que ofrece el número de apariciones de un elemento buscado
demo_list.count(1)

# .append(x) -> Método que añade un elemento a la lista
demo_list.append("dog")

# .extend((x,y,z,...)) -> Método que añade una serie de elementos a una lista (mediante una tupla o lista)
demo_list.extend(("cat", "dog", "fish"))
demo_list.extend(["cat", "dog", "fish"])

# .insert(position, element) -> Método que añade un elemento en una posición
demo_list.insert(1, "pink")
demo_list.insert(len(demo_list), "pink")

# .pop() -> Método que elimina el último elemento (o el indicado)
demo_list.pop() # Último
demo_list.pop(0) # Primero

# .remove() -> Método que elimina el elemento buscado
demo_list.remove("hello")

# .clear() -> Método que limpia la lista
demo_list.clear()

# .sort() -> Método que ordena la lista
demo_list.sort() # Ordena alfabéticamente y de menor a mayor
demo_list.sort(reverse=True) # Ordena al contrario
