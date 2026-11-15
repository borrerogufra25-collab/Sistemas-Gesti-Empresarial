# 5. Crea un conjunto de números enteros leyendo por teclado. Se podrá hacer lo siguiente:
# 1. Añadir el número 15.
# 2. Eliminar el número 9.
# 3. Calcular la cantidad de elementos.
# 4. Comprobar si 6 está en el conjunto.

conjNum = set()
num = 0
agregar = 0

num = int(input('¿Cuántos números quieres añadir al set?'))
for i in range(num):
    agregar = int(input(f'{i+1}º '))
    conjNum.add(agregar)

print(f'El conjunto: {conjNum}')

# 1. Añadir el número 15.

print('Añadimos el número 15')
conjNum.add(15)
print(f'El nuevo conjunto: {conjNum}')

# 2. Eliminar el número 9.

print('Eliminamos el número 9')
if 9 in conjNum:
    conjNum.remove(9)
    print(f'El nuevo conjunto: {conjNum}')
else:
    print('El 9 no está')
    print(f'El nuevo conjunto: {conjNum}')

# 3. Calcular la cantidad de elementos.

print(f'Hay {len(conjNum)} elementos en el conjunto')


# 4. Comprobar si 6 está en el conjunto.

if 6 in conjNum:
    print('El 6 SI está en el set')
else:
    print('El 6 NO está en el set')
