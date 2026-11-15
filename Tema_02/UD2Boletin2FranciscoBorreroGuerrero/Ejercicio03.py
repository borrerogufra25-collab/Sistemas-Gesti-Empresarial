# 3. Crear un diccionario que tenga como claves el dni de un estudiante y como valor la nota media de su
# expediente. La nota media se generará de manera aleatoria entre 1 y 10.
# Escribir el código necesario en un menú para hacer los siguiente:
# a) Mostrar los datos.
# b) Modificar la nota.
# c) Añadir un nuevo estudiante.
# d) Crear un nuevo diccionario (no modificar el original) solo con los estudiantes que tienen nota media
# mayor a un valor dado por teclado (por ejemplo, para comprobar que pueden entrar en un ciclo según esa
# nota de corte).

import random

estudiantes = {
    '12345678A': round(random.uniform(1, 10), 2),
    '12345678B': round(random.uniform(1, 10), 2),
    '12345678C': round(random.uniform(1, 10), 2),
}

while True:
    print('\n1. Mostrar los datos')
    print('2. Modificar la nota')
    print('3. Añadir un nuevo estudiante')
    print('4. Estudiantes con nota media mayor a un valor')
    print('0. Salir')
    opcion = input('Elige una opción: ')

    match opcion:
        case '1':
            print('\nDATOS DE LOS ESTUDIANTES')
            for dni, nota in estudiantes.items():
                print(f'DNI: {dni} | NOTA MEDIA: {nota}')

        case '2':
            dni = input('DNI del estudiante: ').upper()
            if dni in estudiantes:
                try:
                    nueva = float(input('Nueva nota (0-10): '))
                    if 0 <= nueva <= 10:
                        estudiantes[dni] = nueva
                        print('Nota modificada.')
                    else:
                        print('La nota debe estar entre 0 y 10.')
                except ValueError:
                    print('Nota no válida.')
            else:
                print('Ese DNI no existe.')

        case '3':
            dni = input('DNI del nuevo estudiante: ').upper()
            if dni in estudiantes:
                print('Ese DNI ya existe.')
            else:
                estudiantes[dni] = round(random.uniform(1, 10), 2)
                print(f'Estudiante añadido con nota {estudiantes[dni]}')

        case '4':
            try:
                corte = float(input('Nota de corte: '))
                admitidos = {
                    dni: nota for dni, nota in estudiantes.items() if nota > corte
                }
                if admitidos:
                    print(f'\nEstudiantes con nota mayor a {corte}:')
                    for dni, nota in admitidos.items():
                        print(f'DNI: {dni} | NOTA MEDIA: {nota}')
                else:
                    print('Ningún estudiante supera esa nota.')
            except ValueError:
                print('Valor no válido.')

        case '0':
            print('Adiós.')
            break

        case _:
            print('Opción no válida.')
