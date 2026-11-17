palabrasRaras = {"Aro": "De acuerdo", "Pechá": "Cantidad grande"}
endesuso = {}
opcion = 0
significado = ''
palabra = ''
nueva = ''
contador = 0

print('Bienvenido al programa de palabras raras')

while True:
    print('1. Mostrar todo el diccionario.')
    print('2. Mostrar cúantas veces aparece un significado.')
    print('3. Modificar un valor.')
    print('4. Borrar un elemento.')
    print('5. Mostrar palabras endesusos')
    print('6. Buscar una palabra.')
    opcion = int(input('Elija una opción'))

    match opcion:
        case 1:
            for pal, sign in palabrasRaras.items():
                print(f'La palabra "{pal}" significa: {sign}')

        case 2:
            significado = input(f'¿Qué significado quieres buscar?\n')
            for sig in palabrasRaras.values():
                if sig == significado:
                    contador += 1
            if contador == 0:
                print('Significado no encontrado')
            else:
                print(f'Aparece: {contador} vez/veces')
            contador = 0

        # case 3:
        #     significado = input(f'¿Qué significado quieres buscar?\n')
        #     if significado in palabrasRaras:
        #         nueva = input('¿Qué nuevo significado quieres?')
        #         palabrasRaras.values(significado).update(nueva)
        #     else:
        #         palabrasRaras.update(sign)

        # No recuerdo bien como usar el update

        case 4:
            palabra = input(f'¿Qué palabra quieres buscar?\n')
            if palabra in palabrasRaras:
                endesuso = palabrasRaras.pop(palabra)
            else:
                print('Palabra no encontrada')

        case 5:
            print(endesuso)

        case 6:
            palabra = input(f'¿Qué palabra quieres buscar?\n')
            print(palabrasRaras.get(palabra, "No se encuentra"))

        case 0:
            print('¡Hasta pronto!')
            break

        case _:
            print('Opción incorrecta')
