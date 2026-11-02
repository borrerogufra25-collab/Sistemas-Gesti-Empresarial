# 14. Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.


palabra = ''
palabraInvertida = ''


palabra = input("Introduce una palabra: ")

palabraInvertida = palabra[::-1]

if palabra == palabraInvertida:
    print(f"'{palabra}' es un palíndromo.")
else:
    print(f"'{palabra}' no es un palíndromo.")
