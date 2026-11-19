f = open('Tema_03/Ejemplos01_ficheros/archivo.txt')
f2 = open('Tema_03/Ejemplos01_ficheros/files/archivoCarpeta.txt')

texto1 = f.readlines()
texto2 = f2.read()

print(texto1)
print(f'\n', texto2)
