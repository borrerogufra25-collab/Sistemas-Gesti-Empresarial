# 14) Crea una función en Python llamada triangulo, que reciba un
# número entero e imprima un patrón como este por pantalla.

hasta = int(input('¿Hasta cuando quieres llegar?'))
piramide = str('')

while len(piramide) != hasta:
    piramide += '*'
    print(piramide)

# while len(piramide) != 0:
#     piramide -= piramide.end
#     print(piramide)
