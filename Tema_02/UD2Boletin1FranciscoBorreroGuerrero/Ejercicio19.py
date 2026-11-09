# 19. Crear un programa que lea los precios de 5 artículos y las cantidades vendidas por una empresa
# en sus 4 sucursales. Informar de:
# • Las cantidades totales de cada artículo.
# • La cantidad de artículos en la sucursal 2.
# • La cantidad del artículo 3 en la sucursal 1.
# • La recaudación total de cada sucursal.
# • La recaudación total de la empresa.
# • La sucursal de mayor recaudación.

numArticulos = 5
numSucursales = 4

precios = []
cantidades = []
totalesArticulo = []
recaudaciones = []

# Leer precio
print('--- PRECIOS ---')
for articulo in range(numArticulos):
    precio = float(input(f'Precio del artículo {articulo + 1}: '))
    precios.append(precio)

# Leer cantidades
for sucursal in range(numSucursales):
    print(f'\n--- SUCURSAL {sucursal + 1} ---')
    fila = []
    for articulo in range(numArticulos):
        cantidad = int(input(f'Cantidad vendida del artículo {articulo + 1}: '))
        fila.append(cantidad)
    cantidades.append(fila)

# Sumar
print('\n--- CANTIDADES TOTALES DE CADA ARTÍCULO ---')
for articulo in range(numArticulos):
    total = 0
    for sucursal in range(numSucursales):
        total += cantidades[sucursal][articulo]
    totalesArticulo.append(total)
    print(f'Artículo {articulo + 1}: {total} unidades')


print(f'\nCantidad de artículos en la sucursal 2: {sum(cantidades[1])}')


print(f'Cantidad del artículo 3 en la sucursal 1: {cantidades[0][2]}')

# Recaudación de cada sucursal
print('\n--- RECAUDACIÓN DE CADA SUCURSAL ---')
for sucursal in range(numSucursales):
    recaudacion = 0
    for articulo in range(numArticulos):
        recaudacion += cantidades[sucursal][articulo] * precios[articulo]
    recaudaciones.append(recaudacion)
    print(f'Sucursal {sucursal + 1}: {recaudacion:.2f} €')

# Recaudación total
print(f'\nRecaudación total de la empresa: {sum(recaudaciones):.2f} €')

# Sucursal de mayor recaudación
mayor = max(recaudaciones)
sucursal_mayor = recaudaciones.index(mayor) + 1
print(f'Sucursal de mayor recaudación: la {sucursal_mayor} ({mayor:.2f} €)')
