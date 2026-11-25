# 3. Haz un programa que copie el contenido de un fichero llamado 'origen.txt' en otro llamado
# 'copia.txt'.

import shutil

f = open('Tema_03/UD2Boletin4FranciscoBorreroGuerrero/Ejercicio03/Ejercicio03.txt')
copy = open('Tema_03/UD2Boletin4FranciscoBorreroGuerrero/Ejercicio03/copia.txt')

shutil.copy(
    'Tema_03/UD2Boletin4FranciscoBorreroGuerrero/Ejercicio03/Ejercicio03.txt',
    'Tema_03/UD2Boletin4FranciscoBorreroGuerrero/Ejercicio03/copia.txt',
)

print('Original:', f.read())
print('Copia:', copy.read())
