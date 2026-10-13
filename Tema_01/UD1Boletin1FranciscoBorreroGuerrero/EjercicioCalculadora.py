# Hacer una calculadora

salir = True
opcion = 0
num1 = 0
num2 = 0

print('Bienvenido a la calculadora')

while salir:
    print('Elija una opción:')
    print('1. Sumar')
    print('2. Restar')
    print('3. Multiplicar')
    print('4. Dividir')
    print('0. Salir')
    opcion = int(input(''))

    match opcion:
        case 1:
            num1 = float(input('Introduzca el primer número a sumar: '))
            num2 = float(input('Introduzca el segundo número a sumar: '))
            print('El resultado es: ', num1 + num2)

        case 2:
            num1 = float(input('Introduzca el primer número a restar: '))
            num2 = float(input('Introduzca el segundo número a restar: '))
            print('El resultado es: ', num1 - num2)

        case 3:
            num1 = float(input('Introduzca el primer número a multiplicar: '))
            num2 = float(input('Introduzca el segundo número a multiplicar: '))
            print('El resultado es: ', num1 * num2)

        case 4:
            num1 = float(input('Introduzca el primer número a dividir: '))
            num2 = float(input('Introduzca el segundo número a dividir: '))
            print('El resultado es: ', num1 / num2)

        case 0:
            salir = False
            print('Hasta luego')

        case _:
            print('Opción incorrecto')
