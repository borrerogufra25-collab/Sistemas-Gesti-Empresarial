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


while True:

    print('1. Guardar nuevo conductor y sus Km')
    print('2. Buscar conductor')
    print('3. Editar conductor')
    print('4. Borrar conductor')
    print('0. Salir')
    opcion = int(input('Elija una opción: '))

    match opcion:

        case 1:
            print('¿Cómo se llama el conductor?')
            nombres.append(input(''))

            print('Ahora añade los kilómetros: ')
            for i, semana in len(semana), semana:
                kms.append(input(f'{semana}: '))

        case 0:
            print('¡Hasta pronto!')

        case _:
            print('Opción incorrecta')
