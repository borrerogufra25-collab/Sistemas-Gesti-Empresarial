# Obtener un elemento

# Igual que en el caso de las cadenas de texto, podemos obtener un elemento de una lista a
# través del índice (lugar) que ocupa. Veamos un ejemplo:

tienda = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']

print('Obtener un elemento')

print(tienda)
print(tienda[0])
print(tienda[1])
print(tienda[2])
print(tienda[-1])  # Igual que se hacían con los String, sacando el índice a la inversa


# Trocear una lista ([start:end:step])
# El troceado de listas funciona de manera totalmente análoga al troceado de cadenas
print('Trocear una lista')

print(tienda[0:3])
print(tienda[:3])
print(tienda[2:4])
print(tienda[-1:-4:-1])
print(tienda[::-1])  # Equivale a invertir la lista
print(list(reversed(tienda)))  # Otra forma de invertir

# MODIFICANDO la lista original
print(tienda.reverse())


# Creando desde vacío
# Una forma muy habitual de trabajar con listas es empezar con una vacía e ir añadiendo
# elementos poco a poco. Se podría hablar de un patrón creación.
print('Creando desde vacío')

numerosPares = []

for i in range(20):
    if i % 2 == 0:
        numerosPares.append(i)

print(numerosPares)


# Repetir elementos
print('Repetir elementos')
print(tienda * 3)
