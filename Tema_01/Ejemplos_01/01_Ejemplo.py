x, y, z = 10, 20, 30

num = 2**4
print(num)

# Se puede operar con los boolean

print(True + 2)  # True = 1
print(False - 1)  # False = 0

# Textos

msg = 'Primera línea\nSegunda línea\nTercera línea'
print(msg)

text = 'abc\ndef'
print(text)
# La diferencia es que con r al principio omite la expresión literal
# El modificador r'' es muy utilizado para la escritura de expresiones regulares.
text = r'abc\ndef'
print(text)

text = 'a\tb\tc'
print(text)

# Más formatos

msg1 = '¿Sabes por qué estoy aquí?'
msg2 = 'Porque me apasiona'

print(msg1, msg2)


print(msg1, msg2, sep='|')

print(msg2, end='!!')

# Tabulador
msg = Valor = '\t40'
print(msg)
Valor = 40
# Comilla simple
msg = 'Necesitamos \escapar\ la comilla simple'
print(msg)
'Necesitamos escapar la comilla simple'
# Barra invertida
msg = 'Capítulo \\ Sección \\ Encabezado'
print(msg)
'Capítulo \ Sección \ Encabezado'
