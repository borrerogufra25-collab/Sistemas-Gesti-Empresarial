f = open('Tema_03/Ejemplos01_ficheros/archivo.txt')
f2 = open('Tema_03/Ejemplos01_ficheros/files/archivoCarpeta.txt')

# Lectura de ficheros, entero o por líneas

textoEntero = f2.read()
textoLineaALinea = f.readlines()

print(textoEntero)
print(f'\n', textoLineaALinea)


# Lectura línea a línea
f.seek(0)  # Esto hace que vuelva al principio del fichero
for line in f:
    print(line)


# Lectura de una línea
f.seek(0)  # Esto hace que vuelva al principio del fichero
for line in f:
    print('Esto es una línea', line)
    break
