# Trocear una cadena
# Es posible extraer «trozos» («rebanadas») de una cadena de texto.
# Tenemos varias aproximaciones para ello:
# [:] Extrae la secuencia entera desde el comienzo hasta el final.
# Es una especia de copia de toda la cadena de texto.
# [start:] Extrae desde start hasta el final de la cadena.
# [:end] Extrae desde el comienzo de la cadena hasta end menos 1.
# [start:end] Extrae desde start hasta end menos 1.
# [start:end:step] Extrae desde start hasta end menos 1 haciendo
# saltos de tamaño step.

frase = 'Agua pasada no mueve molino'
print(frase[:])
print(frase[12:])
print(frase[:11])
print(frase[5:11])
print(frase[5:11:2])
