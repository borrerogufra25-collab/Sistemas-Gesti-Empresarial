# Dividir una cadena
# Una tarea muy común al trabajar con cadenas de texto es dividirlas por algún tipo
# de separador. En este sentido, Python nos ofrece la función split(), que debemos usar
# anteponiendo el «string» que queramos dividir:

frase = 'No hay mal que por bien no venga'
print(frase.split())

frase2 = 'Martillo,Sierra,Destornillador'
print(frase2.split(','))

# Existe una forma algo más avanzada de dividir una cadena a través del particionado. Para
# ello podemos valernos de la función partition() que proporciona Python.

a = '3 + 4'
print(a.partition('+'))  # Decimos que el separador va a ser el +
