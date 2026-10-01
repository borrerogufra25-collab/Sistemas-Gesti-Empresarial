temperatura = 28

if temperatura < 20:
    if temperatura < 10:
        print('Nivel azul')
    else:
        print('Nivel verde')
elif temperatura < 30:  # esto es else + if
    print('Nivel naranja')
else:
    print('Nivel rojo')

###################################

# Otra versión

riesgoFuego = 'LOW' if temperatura < 30 else 'HIGH'

# Tradicional es así:

if temperatura < 30:
    riesgoFuego = 'LOW'
else:
    riesgoFuego = 'HIGH'

# Pero esta no es válida, es mejor la anterior

####################################

# Operadores lógicos

x = 8
x > 4 or x > 12  # True or False

x < 4 or x > 12  # False or False

x > 4 and x > 12  # True and False

x > 4 and x < 12  # True and True

not (x != 8)  # not False

#####################################

# «Booleanos» en condiciones

is_cold = False
if not is_cold:  # Equivalente a if is_cold == False
    print('Usa camiseta')
else:
    print('Coge chaqueta')
