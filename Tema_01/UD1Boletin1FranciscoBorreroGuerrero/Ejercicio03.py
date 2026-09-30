# 3) Mostrar el precio final (con IVA) de un producto con un valor de 100 euros, suponiendo que el IVA es el 21%.

precio_base = 0
iva = 0
resultado = precio_base - precio_base * iva / 100

precio_base = float(input('Itroduzca el precio base: '))
iva = float(input('Introduzca el IVA actual: '))
resultado = precio_base - precio_base * iva / 100
print(f'El resultado es: {resultado} €')
