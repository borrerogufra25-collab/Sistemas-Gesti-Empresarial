# Combinar cadenas

proverb1 = 'Cuando el río suena'
proverb2 = 'agua lleva'
print(proverb1 + proverb2)

print(proverb1 + ', ' + proverb2)  # incluimos una coma

# Repetir cadenas

castigo = 'Soy maloso'
print((castigo + ', ') * 4)

# Obtener un carácter
# Los «strings» están indexados y cada carácter tiene su propia posición. Para obtener un
# único carácter dentro de una cadena de texto es necesario especificar su índice dentro de
# corchetes [...].

frase = 'Hola, mundo'
print(frase[0])
print(frase[-1])
print(frase[4])
print(frase[-5])

# En caso de que intentemos acceder a un índice que no existe,
# obtendremos un error por fuera de rango
