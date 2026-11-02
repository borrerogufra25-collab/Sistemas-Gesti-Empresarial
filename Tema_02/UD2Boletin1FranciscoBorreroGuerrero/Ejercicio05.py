# 5. Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga
# cuántas veces aparece esa palabra en la lista.

numPalabras = 0
listaPalabras = []
palabra = ''
buscar = ''
vecesPalabra = 0

numPalabras = int(input("¿Cuántas palabras quieres introducir? "))

for i in range(numPalabras):
    palabra = input(f'Introduce la palabra {i+1}: ')
    listaPalabras.append(palabra)

buscar = input('¿Qué palabra quieres buscar? ')

vecesPalabra = listaPalabras.count(buscar)

print(f"La palabra '{buscar}' aparece {vecesPalabra} veces en la lista.")
