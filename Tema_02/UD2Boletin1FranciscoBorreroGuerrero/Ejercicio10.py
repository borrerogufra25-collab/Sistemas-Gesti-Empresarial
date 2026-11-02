# 10. Escriba un programa que permita crear una lista de palabras y que, a continuación, elimine los elementos
# repetidos (dejando únicamente el primero de los elementos repetidos).


numPalabras = 0
listaPalabras = []
listaSinRepetidos = []
palabra = ''


numPalabras = int(input("¿Cuántas palabras quieres introducir? "))

for i in range(numPalabras):
    palabra = input(f'Introduce la palabra {i+1}: ')
    listaPalabras.append(palabra)


for palabra in listaPalabras:
    if palabra not in listaSinRepetidos:
        listaSinRepetidos.append(palabra)

print("Lista original:", listaPalabras)
print("Lista sin repetidos:", listaSinRepetidos)
