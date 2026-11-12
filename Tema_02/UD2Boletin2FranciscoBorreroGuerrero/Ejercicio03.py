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

opcion = 0

estudiantes = {
    '12345678A': round(random.uniform(1, 10), 2),
    '12345678B': round(random.uniform(1, 10), 2),
    '12345678C': round(random.uniform(1, 10), 2),
}

while True:
    print('1. Mostrar los datos')
    print('2. Modificar la nota.')
    print('3. Añadir un nuevo estudiante.')
    print('4. Estudiantes que tienen nota media mayor a un valor')
    print('0. Salir')
    opcion = input('')

    match opcion:
        case 1:
            print('\nDATOS DE LOS ESTUDIANTES')
            for dni, nota in estudiantes.items():
                print(f'DNI: {dni} | NOTA MEDIA: {nota}')
