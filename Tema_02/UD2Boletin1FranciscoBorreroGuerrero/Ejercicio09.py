# 9. Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista
# igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).

numPalabras = 0
listaPalabras = []
listaInvertida = []
palabra = ''

numPalabras = int(input("¿Cuántas palabras quieres introducir? "))

for i in range(numPalabras):
    palabra = input(f'Introduce la palabra {i+1}: ')
    listaPalabras.append(palabra)

listaInvertida = list(reversed(listaPalabras))

print("Lista original:", listaPalabras)
print("Lista invertida:", listaInvertida)
