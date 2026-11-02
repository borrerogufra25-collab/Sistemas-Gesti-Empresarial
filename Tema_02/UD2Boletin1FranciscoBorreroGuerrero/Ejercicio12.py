# 12. Escriba un programa que permita crear una lista de palabras y que, a continuación, ordene la lista por orden
# alfabético.

numPalabras = 0
listaPalabras = []
listaOrdenada = []
palabra = ''


numPalabras = int(input("¿Cuántas palabras quieres introducir? "))

for i in range(numPalabras):
    palabra = input(f'Introduce la palabra {i+1}: ')
    listaPalabras.append(palabra)

listaOrdenada = sorted(listaPalabras)

print("Lista original:", listaPalabras)
print("Lista ordenada:", listaOrdenada)
