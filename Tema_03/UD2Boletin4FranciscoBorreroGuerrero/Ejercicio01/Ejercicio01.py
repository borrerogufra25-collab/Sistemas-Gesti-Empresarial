# 1. Escribe un programa que cuente cuántas líneas NO vacías contiene un fichero 'entrada.txt' que
# tenga varias líneas de prueba.

f = open('Tema_03/UD2Boletin4FranciscoBorreroGuerrero/Ejercicio01/Ejercicio01.txt')
contador = 1

for line in f:
    if f.readline() == '\n':
        contador += 1
print('Hay ', contador)
