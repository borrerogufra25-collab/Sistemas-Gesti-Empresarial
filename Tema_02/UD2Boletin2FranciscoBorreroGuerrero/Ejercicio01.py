# 1. Dada la tupla temperaturas = (21, 24, 19, 30, 25, 28). Crear el código necesario para:
# 1. Mostrar el valor máximo y mínimo.
# 2. Calcular la temperatura media.
# 3. Convertir la tupla en lista, añadir una nueva temperatura y volver a convertir a tupla.
# 4. Comprobar si 30 está presente.

temperaturas = (21, 24, 19, 30, 25, 28)
opcion = 0
temp = 0, 0
probar = 0, 0

while True:
    print('1. Mostrar el valor máximo y mínimo.')
    print('2. Calcular la temperatura media.')
    print(
        '3. Convertir la tupla en lista, añadir una nueva temperatura y volver a convertir a tupla.'
    )
    print('4. Comprobar si está presente.')
    print('0. Salir')
    opcion = int(input(''))
    match opcion:
        case 1:
            print('La temperatura máxima es: ') + max(temperaturas) + ('º')
            print('La temperatura mínima es: ') + min(temperaturas) + ('º')

        case 2:
            (
                print('La temperatura media es: ')
                + sum(temperaturas) / len(temperaturas)
                + ('º')
            )

        case 3:
            temp = float(input('¿Qué temperatura quieres añadir?'))
            list(temperaturas).append(temp)
            tuple(temperaturas)

        case 4:
            probar = float(input('¿Qué temperatura quieres comprobar'))

            if probar in temperaturas:
                print('Si está')
            else:
                print('No está')

        case 0:
            print('¡Hasta pronto!')
            break

        case _:
            print('Opción incorrecta')
