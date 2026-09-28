# Pertenencia de un elemento

# Si queremos comprobar que una determinada subcadena se
# encuentra en una cadena de texto utilizamos el
# operador in para ello. Se trata de una expresión que
# tiene como resultado un valor «booleano» verdadero o falso:

frase = 'Más vale malo conocido que bueno por conocer'

print('malo' in frase)
print('bueno' in frase)
print('regular' in frase)

# Habría que prestar atención al caso en el que intentamos
# descubrir si una subcadena no está en la cadena de texto:

frase2 = 'ATGAAATTGAAATGGGA'

print('C' in frase2)
print('C' not in frase2)
