# 11. Escriba un programa que permita crear dos listas de palabras y que, a continuación, escriba las siguientes
# listas (en las que no debe haber repeticiones):
# Lista de palabras que aparecen en las dos listas.
# Lista de palabras que aparecen en la primera lista, pero no en la segunda.
# Lista de palabras que aparecen en la segunda lista, pero no en la primera.
# Lista de palabras que aparecen en ambas listas.


numPalabras1 = 0
numPalabras2 = 0
lista1 = []
lista2 = []
enAmbas = []
soloPrimera = []
soloSegunda = []
enAlguna = []
palabra = ''

numPalabras1 = int(input("¿Cuántas palabras tendrá la primera lista? "))

for i in range(numPalabras1):
    palabra = input(f'Lista 1 - Introduce la palabra {i+1}: ')
    lista1.append(palabra)

numPalabras2 = int(input("¿Cuántas palabras tendrá la segunda lista? "))

for i in range(numPalabras2):
    palabra = input(f'Lista 2 - Introduce la palabra {i+1}: ')
    lista2.append(palabra)

for palabra in lista1:
    if palabra in lista2 and palabra not in enAmbas:
        enAmbas.append(palabra)

for palabra in lista1:
    if palabra not in lista2 and palabra not in soloPrimera:
        soloPrimera.append(palabra)

for palabra in lista2:
    if palabra not in lista1 and palabra not in soloSegunda:
        soloSegunda.append(palabra)

for palabra in lista1 + lista2:
    if palabra not in enAlguna:
        enAlguna.append(palabra)

print("En las dos listas:", enAmbas)
print("Solo en la primera:", soloPrimera)
print("Solo en la segunda:", soloSegunda)
print("En alguna de las dos:", enAlguna)
