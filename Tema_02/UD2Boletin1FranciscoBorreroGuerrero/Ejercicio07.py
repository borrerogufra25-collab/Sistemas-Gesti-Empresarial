# 7. Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine
# esa palabra de la lista.

numPalabras = 0
listaPalabras = []
palabra = ''
palabraEliminar = ''

numPalabras = int(input("¿Cuántas palabras quieres introducir? "))

for i in range(numPalabras):
    palabra = input(f'Introduce la palabra {i+1}: ')
    listaPalabras.append(palabra)


palabraEliminar = input("¿Qué palabra quieres eliminar? ")

if palabraEliminar in listaPalabras:
    listaPalabras.remove(palabraEliminar)
else:
    print("Esa palabra no está en la lista.")

print("La lista nueva es: ", listaPalabras)
