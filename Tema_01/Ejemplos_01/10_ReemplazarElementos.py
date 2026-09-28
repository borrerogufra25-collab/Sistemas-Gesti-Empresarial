# Podemos usar la función replace() indicando la subcadena a reemplazar, la subcadena
# de reemplazo y cuántas instancias se deben reemplazar. Si no se especifica este último
# argumento, la sustitución se hará en todas las instancias encontradas:

a = 'Quien mal anda mal acaba'

print(a.replace('mal', 'bien'))

print(a.replace('mal', 'bien', 1))  # sólo 1 reemplazo)
