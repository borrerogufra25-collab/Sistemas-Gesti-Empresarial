# 11) Escribe un programa que pida primero un número entero
# y después pida números enteros hasta que la suma de los
# números introducidos coincida con el número inicial.
# El programa termina escribiendo la lista de números.

final = int(input('Introduce el número inicial: '))
suma = 0
numeros = []

while suma <= final:
    num = int(input('Introduce un número: '))
    suma += num
    numeros.append(num)

print('Lista de números introducidos:', numeros, 'La suma es: ', suma)
