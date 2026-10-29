# 16. Queremos desarrollar un pequeño programa que ayude a un técnico meteorológico (mi amigo Nico es
# meteorólogo) a analizar las temperaturas registradas durante una semana en su estación de trabajo.
# Rellenar la lista con temperaturas generadas de forma aleatoria entre dos límites leídos por teclado. Pueden
# tener decimales.
# A partir de esa lista, el programa debe:
# Mostrar todas las temperaturas introducidas.
# Calcular y mostrar la temperatura media.
# Mostrar la temperatura máxima y mínima junto con el día en que ocurrieron (día 1, día 2, no usar fechas).
# Ordena la lista de mayor a menor temperatura.
# Mostrar cuántos días tuvieron temperaturas por encima de la media.
# Crear una nueva lista solo con las temperaturas superiores a la media.

import random

temperaturas = [random.uniform(-10.99, 49.99) for _ in range(10)]
temperaturaMaxMedia = []
media = 0.0
opcion = 0

while True:
    print('1. Mostrar todas las temperaturas')
    print('2. Calcular temperatura media')
    print('3. Mostrar temperatura máxima y mínima')
    print('4. Ordenar temperaturas')
    print('5. Mostrar cuántos días tuvieron temperaturas por encima de la media.')
    print('0. Salir')
    opcion = int(input(''))

    match opcion:
        case 1:
            print('Estas son las temperaturas: ')
            for indice, temp in enumerate(temperaturas):
                print(f'{indice + 1}º día: {temp:.2f}º\n')

        case 2:
            media = sum(temperaturas) / len(temperaturas)
            print(f'\nLa temperatura media es: {media:.2f}º\n')

        case 3:
            print(f'\nLa temperatura máxima es: {max(temperaturas):.2f}º\n')
            print(f'La temperatura mínima es: {min(temperaturas):.2f}º\n')

        case 4:
            print('\nTemperaturas ordenadas:')
            for i in sorted(temperaturas):
                print(f'{i:.2f}º\n')

        case 5:
            print(f'\nTemperaturas por encima de la media ({media:.2f}º)\n')
            for i in temperaturas:
                if i > media:
                    temperaturaMaxMedia.append(i)
            for i in temperaturaMaxMedia:
                print(f'{i:.2f}º\n')

        case 0:
            print('¡Hasta pronto!')
            break

        case _:
            print('\nOpción incorrecta\n')
