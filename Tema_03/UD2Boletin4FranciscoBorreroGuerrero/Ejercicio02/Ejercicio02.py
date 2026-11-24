from datetime import datetime

# 2. Crea un programa que añada la fecha y hora actuales al final de un fichero.

f = open('Tema_03/UD2Boletin4FranciscoBorreroGuerrero/Ejercicio02/Ejercicio02.txt', 'a')
hora = datetime.now()
horaFormateada = hora.strftime("%d/%m/%Y %H:%M")

f.write(horaFormateada + '\n')
f.close()

f = open('Tema_03/UD2Boletin4FranciscoBorreroGuerrero/Ejercicio02/Ejercicio02.txt')
print(f.read())
