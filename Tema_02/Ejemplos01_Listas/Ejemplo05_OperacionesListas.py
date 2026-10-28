# Longitud de una lista
# Podemos conocer el número de elementos que tiene una lista con la función len():

shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
print(len(shopping))


# Iterar sobre una lista
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
for product in shopping:
    print(product)


# Iterar usando enumeración
# Hay veces que no sólo nos interesa «visitar» cada uno de los elementos de una lista, sino
# que también queremos saber su índice dentro de la misma. Para ello Python nos ofrece la
# función enumerate():
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
for i, product in enumerate(shopping):
    print(i, product)


# Iterar sobre múltiples listas
# Python ofrece la posibilidad de iterar sobre múltiples listas en paralelo utilizando la
# función zip(). Se basa en ir «juntando» ambas listas elemento a elemento:
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
details = ['mineral natural', 'de oliva virgen ', 'basmati']
for product, detail in zip(shopping, details):
    print(product, detail)
# Como dato, se para en la lista más corta
