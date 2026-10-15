# 1)

opcion = 0
horasSemana = 0.0
horasSobra = 0.0
horasDiariasTotal = 0.0
contador = 0
cafe = 0

print('Bienvenido al gestor de sueños (para dormir)\n')

while True:

    print('1. Calculadora de presupuesto de descanso semanal')
    print('2. Diagnóstico del desarrollador')
    print('3. Salir')
    opcion = int(input(''))
    match opcion:

        case 1:
            while True:
                print('1. ¿Cuántas horas de sueño necesitas a la semana para rendir?')
                print('2. ¿Cuántas horas has dormido cada día?')
                print('3. Saber cuantas horas de siesta tengo')
                print('4. Salir')
                opcion = int(input(''))
                match opcion:

                    case 1:
                        horasSemana = float(
                            input(
                                'Indique las horas necesarias de sueño a la semana: \n'
                            )
                        )

                    case 2:
                        while horasSemana > horasDiariasTotal or contador != 7:
                            contador = contador + 1
                            horasDiariasTotal += float(
                                input('Indique cuantas horas por día: \n')
                            )

                    case 3:
                        horasSobra = horasSemana - horasDiariasTotal

                        if horasSobra > 0:
                            print('Te quedan de horas extras: ', horasSobra)
                        else:
                            print('Alerta por agotamiento')

                    case 4:
                        break

                    case _:
                        print('Opción incorrecta')

        case 2:
            while True:
                print('1. ¿Cuántas tazas de café/bebidas energéticas ha tomado hoy?')
                print('2. Saber mi modo')
                print('3. Saber mi entrés')
                print('4. Salir')
                opcion = int(input(''))

                match opcion:
                    case 1:
                        cafe = int(input('Indique cuántas bebidas llevas\n'))

                    case 2:
                        if cafe <= 1:
                            print('Modo batería baja')
                        elif cafe >= 2 or cafe <= 4:
                            print('Rendimiento óptimo')
                        else:
                            print(
                                'Escribiendo código a la velocidad de la luz/colapso inminente'
                            )

                    case 3:
                        for _ in range(cafe):
                            print('¡Bugg!')

                    case 4:
                        break

                    case _:
                        print('Opción incorrecta')

        case 3:
            print('¡Hasta pronto!')
            break
