# 3. Se quiere realizar un programa que lea por teclado las distintas notas obtenidas por un alumno (comprendidas
# entre 0 y 10). A continuación, debe mostrar todas las notas a modo boletín de calificaciones, la nota media, la
# nota más alta que ha sacado, la menor y el número de suspensos.

opcion = 0
notas = []
nota = 0.0
cantidadNotas = 0
media = 0
suspensos = 0

print('Buenas, este programa trabaja con tus notas. Elija la opción')


while True:
    print('\n\n1. Añadir notas')
    print('2. Ver todas las notas')
    print('3. Ver nota media')
    print('4. Ver la nota más alta')
    print('5. Ver la nota más baja')
    print('6. Ver los suspensos')
    print('7. Imprimir boletín')
    print('0. Salir')
    opcion = int(input('Elija opción: '))

    match opcion:
        case 1:
            cantidadNotas = int(input('¿Cuántas notas vas a añadir?'))
            print('Perfecto, ahora añade las notas: ')
            for i in range(cantidadNotas):
                nota = float(input(f'{i+1}º nota: '))
                notas.append(nota)

        case 2:
            print(notas)

        case 3:
            media = sum(notas) / len(notas)
            print(f'La nota media es: {media:.2f}')

        case 4:
            print('La nota más alta es:', max(notas))

        case 5:
            print('La más baja es: ', min(notas))

        case 6:
            for nota in notas:
                if nota < 5:
                    suspensos += 1
            print('Número de suspensos: ', suspensos)
            suspensos = 0

        case 7:
            media = sum(notas) / len(notas)
            suspensos = 0
            for nota in notas:
                if nota < 5:
                    suspensos += 1

            print('=' * 30)
            print('   BOLETÍN DE CALIFICACIONES')
            print('=' * 30)
            for numero, nota in enumerate(notas, start=1):
                print(f'Nota {numero:<3}: {nota:>6.2f}')
            print('-' * 30)
            print(f'Nota media : {media:>6.2f}')
            print(f'Nota más alta : {max(notas):>6.2f}')
            print(f'Nota más baja : {min(notas):>6.2f}')
            print(f'Suspensos : {suspensos:>6}')
            print('=' * 30)

        case 0:
            print('Hasta pronto')
            break

        case _:
            print('Opción incorrecta')
