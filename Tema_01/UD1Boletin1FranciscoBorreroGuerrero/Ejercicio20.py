# Haga un programa de la interfaz de un cajero automático. Tendrá las opciones, ver saldo,
# retirar dinero, comprar entradas e ingresar dinero. En cada opción se pedirán los datos
# necesarios y se realizarán las operaciones adecuadas. El coste de las entradas se debe restar al
# saldo de dicha cuenta. La cuenta será creada por nosotros con un saldo inicial concreto.

salir = True
opcion = 0
saldo = 2323.65
operacion = 0.0
entrada = 56.74

print('Bienvenido Usuario, soy un cajero')

while salir:
    print('\n\nIngrese la opción que desee:\n')
    print('1. Ver saldo')
    print('2. Retirar dinero')
    print('3. Ingresar dinero')
    print('4. Comprar entradas para Shakira')
    print('0. Salir')
    opcion = int(input('\n'))

    match opcion:
        case 1:
            print(f'\nSu saldo es: {saldo:.2f}')

        case 2:
            operacion = float(
                input(f'¿Cuánto quieres retirar? Su saldo actual: {saldo:.2f}€\n')
            )
            if operacion > saldo:
                print(f'No puedes retirar tanto. Su saldo: {saldo:.2f}€')
            else:
                saldo = saldo - operacion
                print(f'Su nuevo saldo es: {saldo:.2f}€')

        case 3:
            operacion = float(input('¿Cuánto va a ingresar?\n'))
            saldo = saldo + operacion
            print(f'Su nuevo saldo es: {saldo:.2f}€')

        case 4:
            operacion = 0
            operacion = int(input('¿Cuántas entradas quieres?\n'))
            operacion = entrada * operacion

            if operacion > saldo:
                print(
                    f'No puedes permitírtelo. Su saldo: {saldo:.2f}€ y las entradas valen: {operacion:.2f}€'
                )
            else:
                saldo = saldo - operacion
                print(f'Entradas compradas por: {operacion:.2f}')

        case 0:
            print('\n¡Hasta pronto!')
            salir = False
