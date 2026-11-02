# 6. Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y
# sustituya la primera por la segunda en la lista.

numPalabras = 0
listaPalabras = []
palabra = ''
vieja = ''
nueva = ''

numPalabras = int(input("¿Cuántas palabras quieres introducir? "))

for i in range(numPalabras):
    palabra = input(f'Introduce la palabra {i+1}: ')
    listaPalabras.append(palabra)

vieja = input("¿Qué palabra quieres sustituir? ")
nueva = input("¿Por qué palabra la quieres sustituir? ")

for i in range(numPalabras):
    if listaPalabras[i] == vieja:
        listaPalabras[i] = nueva

print("La lista resultante es:", listaPalabras)
