# 15. Determine si una cadena de texto dada es un isograma, es decir, no se repite ninguna letra.
# Ejemplos válidos de isogramas:
# background
# downstream
# six-year-old


palabra = ''
letrasVistas = []
esIsograma = True


palabra = input("Introduce una cadena de texto: ")

for caracter in palabra:
    if caracter.isalpha():
        if caracter in letrasVistas:
            esIsograma = False
        else:
            letrasVistas.append(caracter)

if esIsograma:
    print(f"'{palabra}' es un isograma.")
else:
    print(f"'{palabra}' no es un isograma.")
