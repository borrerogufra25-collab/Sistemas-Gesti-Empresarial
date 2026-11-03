# Creando tuplas

# Podemos pensar en crear tuplas tal y como lo hacíamos con listas, pero usando paréntesis
# en lugar de corchetes:

empty_tuple = ()
tenerife_geoloc = (28.46824, -16.25462)
three_wise_men = ('Melchor', 'Gaspar', 'Baltasar')

print(empty_tuple)
print(tenerife_geoloc)
print(three_wise_men)


# Tuplas de un elemento
# Hay que prestar especial atención cuando vamos a crear una tupla de un único elemento.
# La intención primera sería hacerlo de la siguiente manera:

oneItemTuple = 'Papá Noel'
print(oneItemTuple)
print(type(oneItemTuple))

# Realmente, hemos creado una variable de tipo str (cadena de texto). Para crear una tupla
# de un elemento debemos añadir una coma al final:
oneItemTuple = ('Papá Noel',)
print(type(oneItemTuple))

# Hay veces que nos podemos encontrar tuplas sin paréntesis


# Conversión
# Para convertir otros tipos de datos en una tupla podemos usar la función tuple():

shopping = ['Agua', 'Aceite', 'Arroz']
print(tuple(shopping))


# Operaciones con tuplas

# Con las tuplas podemos realizar todas las operaciones que vimos con listas salvo las que
# conlleven una modificación «in-situ» de la misma:

frutas = ("manzana", "platano", "cereza")

print(frutas[0])
print(len(frutas))
print("cereza" in frutas)

# Concatenar crea una nueva tupla
mas_frutas = frutas + ("naranja",)
print(mas_frutas)

# 2. OPERACIONES PROHIBIDAS (darán error)
# frutas.append("pera")   # Error: no existe append
# frutas.sort()           # Error: no existe sort
# frutas.remove("platano")# Error: no existe remove
# frutas[0] = "uva"       # Error: no se pueden cambiar valores


# Desempaquetado de tuplas
# El desempaquetado es una característica de las tuplas que nos permite asignar una tupla
# a variables independientes:

three_wise_men = ('Melchor', 'Gaspar', 'Baltasar')
King1, king2, king3 = three_wise_men

print(King1)
print(king2)
print(king3)


# Intercambio de valores
# A través del desempaquetado de tuplas podemos llevar a cabo el intercambio de los valores
# de dos variables de manera directa:
v1 = 40
v2 = 20

v1, v2 = v2, v1

print(v1)
print(v2)
