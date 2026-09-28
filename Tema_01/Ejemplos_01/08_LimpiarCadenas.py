# Limpiar cadenas
# Sirve para limpiar los caracteres de relleno al comienzo
# y al final de los String

copiado = '\n\t \n 48374983274832 \n\n\t \t \n'

print(copiado)
print(copiado.strip())

# Si no se especifican los caracteres a eliminar, strip() usa por defecto cualquier
# combinación de espacios en blanco, saltos de línea \n y tabuladores \t.

# A continuación vamos a hacer «limpieza» por la izquierda (comienzo) y por la derecha (final)
# utilizando la función lstrip() y rstrip() respectivamente:

# «Left strip»
print(copiado.lstrip())

# «Right strip»
print(copiado.rstrip)

# Como habíamos comentado, también existe la posibilidad de especificar los caracteres que
# queremos borrar:

print(copiado.strip('\n'))
