letra = '''Quizás porque mi niñez
... Sigue jugando en tu playa
... Y escondido tras las cañas
... Duerme mi primer amor
... Llevo tu luz y tu olor
... Por dondequiera que vaya'''

# Comprobar si una cadena de texto empieza o termina por alguna subcadena:
print(letra.startswith('Quizás'))
print(letra.endswith('Final'))


# Encontrar la primera ocurrencia de alguna subcadena:
print(letra.find('amor'))
print(letra.index('amor'))

# Tanto find() como index() devuelven el índice de la primera ocurrencia

# Contabilizar el número de veces que aparece una subcadena:
print(letra.count('mi'))
print(letra.count('tu'))
print(letra.count('él'))
