# Escriba un programa en Python que acepte la opción de dos jugadores en
# Piedra-Papel-Tijera y decida el resultado (solución).

# • Entrada: person1=piedra; person2=papel
# • Salida: Gana persona2: El papel envuelve a la piedra

pj1 = 0
pj2 = 0

print('Vamos a jugar al piedra, papel o tijera\n')
pj1 = int(input('Jugador 1 elija: 1 para piedra | 2 para papel | 3 para tijera:\n'))
pj2 = int(input('Jugador 2 elija: 1 para piedra | 2 para papel | 3 para tijera:\n'))


match pj1:
    case 1:
        match pj2:
            case 1:
                print('Es empate, los dos elegisteis piedra')
            case 2:
                print('Gana el jugador 2, el papel gana a la piedra')
            case 3:
                print('Gana el jugador 1, la piedra gana a las tijeras')
    case 2:
        match pj2:
            case 1:
                print('Gana el jugador 1, el papel gana a la piedra')
            case 2:
                print('Es empate, los dos elegisteis papel')
            case 3:
                print('Gana el jugador 2, las tijeras gana al papel')
    case 3:
        match pj2:
            case 1:
                print('Gana el jugador 2, la  piedra gana al papel')
            case 2:
                print('Gana el jugador 1, las tijeras ganan al papel')
            case 3:
                print('Es empate, los dos elegisteis tijeras')
