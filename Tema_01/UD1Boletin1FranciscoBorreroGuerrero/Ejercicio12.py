# 12) Escribe un programa que genere un número aleatorio entre 0 y 10
# y nos pida adivinarlo Tenemos 3 intentos. Puedes mirar el tutorial
# inicial de Python que usamos para instalar VS Code e instalar la biblioteca numpy.

import numpy as np

numAleatorio = np.random.randint(0, 10)
intentos = 3
oportunidad = 0

while intentos > 0:
    oportunidad = int(input("Adivina el número del 0 al 10: "))

    if oportunidad == numAleatorio:
        print("¡Has acertado!")
    else:
        intentos -= 1
        if intentos > 0:
            print("Incorrecto, te quedan ", intentos, " intentos")
        else:
            print("Has perdido. El número era: ", numAleatorio)
