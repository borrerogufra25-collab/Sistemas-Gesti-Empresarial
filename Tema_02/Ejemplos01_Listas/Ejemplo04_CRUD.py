tienda = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
# CRUD

print('Añadir')

# Añadir al final de la lista
print('Añadir al final de la lista')

tienda.append('Atún')
print(tienda)

# Añadir en cualquier posición de una lista
print('Añadir en cualquier posición de una lista')

tienda.insert(1, 'Jamón')
print(tienda)
tienda.insert(3, 'Queso')
print(tienda)

# Borrar elementos

print('Borrar')

# Por su índice: Mediante la sentencia del:

del tienda[3]
print(tienda)

# Por su valor: Mediante la función remove():
tienda.remove('Agua')
print(tienda)

# Por su índice (con extracción): La sentencia del y la función remove() efectivamente
# borran el elemento indicado de la lista, pero no «devuelven»3 nada. Sin embargo,
# Python nos ofrece la función pop() que además de borrar, nos «recupera» el elemento;
# algo así como una extracción. Lo podemos ver como una combinación de acceso +
# borrado:

shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
product = shopping.pop()  # shopping.pop(-1)

print(shopping)

product = shopping.pop(2)

print(shopping)

# Nota: Si usamos la función pop() sin pasarle ningún argumento, por defecto usará
# el índice -1, es decir, el último elemento de la lista. Pero también podemos indicarle el
# índice del elemento a extraer.


# Por su rango: Mediante troceado de listas:
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
shopping[1:4] = []
print(shopping)


# Borrado completo de la lista
# 1. Utilizando la función clear():

shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
print(shopping)
shopping.clear()  # Borrado in-situ
print(shopping)

# 2. «Reinicializando» la lista a vacío con []:
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
print(shopping)
shopping = []  # Nueva zona de memoria (No recomendable)
print(shopping)


# Encontrar un elemento
# Si queremos descubrir el índice
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
print(shopping.index('Huevos'))


# Pertenencia de un elemento
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
print('Aceite' in shopping)
print('Pollo' in shopping)
