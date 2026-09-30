# Identificando caracteres

# Hay veces que recibimos información textual de distintas fuentes y necesitamos
# identificar qué tipo de caracteres contienen. Para ello, Python nos ofrece
# un grupo de funciones muy útiles.

# Lista 8: Detectar si todos los caracteres son letras o números

print('R2D2'.isalnum())
print('C3-PO'.isalnum())

# Lista 9: Detectar si todos los caracteres son números

print('314'.isnumeric())
print('3.14'.isnumeric())

# Lista 10: Detectar si todos los caracteres son letras

print('abc'.isalpha())
print('a-b-c'.isalpha())

# Lista 11: Detectar mayúsculas/minúsculas

print('BIG'.isupper())
print('small'.islower())
print('First Heading'.istitle())
