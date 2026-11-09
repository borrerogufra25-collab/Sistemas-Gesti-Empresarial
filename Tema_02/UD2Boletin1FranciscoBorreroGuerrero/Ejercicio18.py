# 18. En una empresa de transporte se quiere guardar el nombre de los conductores que tiene y los kilómetros
# que conducen cada día de la semana. Para guardar esta información se van a utilizar dos listas:
# • Nombre: Lista para guardar los nombres de los conductores.
# • kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
# Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realiza cada conductor.
# Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.

opcion = 0
nombres = []
kms = []
total_kms = []
semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
buscar = ''


while True:

    print('1. Guardar nuevo conductor y sus Km')
    print('2. Buscar conductor')
    print('3. Editar conductor')
    print('4. Borrar conductor')
    print('5. Mostrar todos')
    print('0. Salir')
    opcion = int(input('Elija una opción: '))

    match opcion:

        case 1:
            print('\n¿Cómo se llama el conductor?\n')
            nombres.append(input(''))

            print('\nAhora añade los kilómetros: \n')
            for dia in semana:
                print(f'{dia}: ')
                i = float(input(''))
                kms.append(i)
            total_kms.append(sum(kms))
            kms.clear()

        case 2:
            buscar = input('\n¿Qué conductor quieres buscar?\n')
            if buscar in nombres:
                print(
                    f'\n{buscar} tiene un total de: {total_kms[nombres.index(buscar)]} km\n'
                )
            else:
                print('\nConductor no encontrado\n')

        case 3:
            buscar = input('\n¿Qué conductor quieres editar?\n')
            if buscar in nombres:
                posicion = nombres.index(buscar)

                nuevo_nombre = input('\nNuevo nombre (Enter para mantener el actual): ')
                if nuevo_nombre != '':
                    nombres[posicion] = nuevo_nombre

                print('\nAñade de nuevo los kilómetros: \n')
                for dia in semana:
                    print(f'{dia}: ')
                    i = float(input(''))
                    kms.append(i)
                total_kms[posicion] = sum(kms)
                kms.clear()

                print('\nConductor actualizado\n')
            else:
                print('\nConductor no encontrado\n')

        case 4:
            buscar = input('\n¿Qué conductor quieres borrar?\n')
            if buscar in nombres:
                posicion = nombres.index(buscar)

                nombres.pop(posicion)
                total_kms.pop(posicion)
                print('\nConductor borrado\n')
            else:
                print('\nConductor no encontrado\n')

        case 5:
            print('\nConductores y kilómetros realizados:')
            for posicion in range(len(nombres)):
                print(f'{nombres[posicion]}: {total_kms[posicion]} km')

        case 0:

            print('¡Hasta pronto!')
            break

        case _:
            print('Opción incorrecta')
