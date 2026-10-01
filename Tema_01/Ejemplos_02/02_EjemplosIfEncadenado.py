op = 0

print('Piensa en un personaje de Marvel y lo adivinaré')

op = int(input('¿Puede volar?\n1. Si\t0. No\n'))
if op == 1:
    op = int(input('¿Es humano?\n1. Si\t0. No\n'))
    if op == 1:
        op = int(input('¿Usa máscara?\n1. Si\t0. No\n'))
        if op == 1:
            print('Es Ironman')
        else:
            print('Es Capitana Marvel')
    else:
        op = op = int(input('¿Usa máscara?\n1. Si\t0. No\n'))
        if op == 1:
            print('Es Ronan el Acusador')
        else:
            print('Visión')
else:
    op = int(input('¿Es humano?\n1. Si\t0. No\n'))
    if op == 1:
        op = int(input('¿Usa máscara?\n1. Si\t0. No\n'))
        if op == 1:
            print('Es Spiderman')
        else:
            print('Es Hulk')
    else:
        op = int(input('¿Usa máscara?\n1. Si\t0. No\n'))
        if op == 1:
            print('Es Rayo Negro')
        else:
            print('Es Thano\ns')
