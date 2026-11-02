# 4. Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un
# número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir
# la lista.

numPalabras = 0
listaPalabras = []
palabra = ''

numPalabras = int(input("¿Cuántas palabras quieres introducir? "))

for i in range(numPalabras):
    palabra = input(f'Introduce la palabra {i+1}: ')
    listaPalabras.append(palabra)

print('La lista de palabras es: ', listaPalabras)
