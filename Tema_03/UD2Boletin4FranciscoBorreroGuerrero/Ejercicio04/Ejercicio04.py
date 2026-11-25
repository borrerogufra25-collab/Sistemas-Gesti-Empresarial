# 4. Crea un programa que lea un fichero llamado 'texto.txt' y genere 'numerado.txt' con todas las líneas
# precedidas de su número.

f = open('Tema_03/UD2Boletin4FranciscoBorreroGuerrero/Ejercicio04/texto.txt')
fNumerado = open(
    'Tema_03/UD2Boletin4FranciscoBorreroGuerrero/Ejercicio04/numerado.txt', 'w+'
)
contador = 0

while True:
    linea = f.readline()
    if not linea:
        break

    contador += 1
    linea = str(contador) + '. - ' + linea
    fNumerado.write(linea)

f.seek(0)
fNumerado.seek(0)

print(f.read())
print(fNumerado.read())


f.close()
fNumerado.close()
