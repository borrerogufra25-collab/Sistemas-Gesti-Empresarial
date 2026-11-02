# 8. Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera
# lista los nombres que haya en la segunda lista.

numPalabras = 0
lista1 = []
lista2 = []
palabra = ''


numPalabras = int(input("¿Cuántas palabras tendrá la primera lista? "))

for i in range(numPalabras):
    palabra = input(f'Lista 1 - Introduce la palabra {i+1}: ')
    lista1.append(palabra)


numPalabras = int(input("¿Cuántas palabras tendrá la segunda lista? "))

for i in range(numPalabras):
    palabra = input(f'Lista 2 - Introduce la palabra {i+1}: ')
    lista2.append(palabra)


for palabra in lista2:
    while palabra in lista1:
        lista1.remove(palabra)

print("Lista 1 resultante:", lista1)
print("Lista 2:", lista2)
