# Voy a alquilar una habitación de mi casa a modo de apartamento turístico y necesito un programa para gestionar lo
# recaudado. Se debe usar una lista como estructura principal para guardar los datos (si hace falta alguna tupla se puede
# usar). Como no hemos dado todavía objetos, lo haremos con una lista de flotantes, que será lo recaudado cada día que lo
# alquilo.
# El programa puede empezar creando una lista directamente con datos y luego poder hacer lo siguiente mediante un menú
# en la clase Principal y debe mostrar en la misma
# • Agregar una nueva recaudación.
# • Poner a cero una recaudación (se me ha ido el cliente sin pagar).
# • Imprimir toda la lista, es decir, mostrar todos los datos de todas las recaudaciones en bonito.
# • Buscar el día en que más he ganado y decir cuántos días he ganado esa cantidad.
# • Sumar una cantidad a un día como gasto extra.
# • Calcular cuánto he recaudado en todas las recaudaciones.
# • Ordenar la lista de mayor a menor.
# • Calcular la media diaria.
# • Calcular el porcentaje de días al mes (suponiendo 30 días) en que he tenido la habitación alquilada.
# • Dividir la lista en dos nuevas listas. Una de ellas debe ser la que tenga las 5 menores recaudaciones, la otra las restantes.
import random

recaudado = [random.uniform(1, 500) for _ in range(10)]
opcion = 0
cantidad = 0.0
maximo = 0.0
contador = 0
alquilados = 0


print('Bienvenido al gestor de recaudación')
while True:
    print('1. Agregar una nueva recaudación.')
    print('2. Poner a cero una recaudación.')
    print('3. Imprimir todas las recaudaciones.')
    print(
        '4. Buscar el día en que más he ganado y decir cuántos días he ganado esa cantidad.'
    )
    print('5. Sumar una cantidad a un día como gasto extra.')
    print('6. Calcular cuánto he recaudado en todas las recaudaciones.')
    print('7. Ordenar la lista de mayor a menor.')
    print('8. Calcular la media diaria.')
    print(
        '9. Calcular el porcentaje de días al mes (suponiendo 30 días) en que he tenido la habitación alquilada.'
    )
    print('10. Las 5 menores recaudaciones, la otra las restantes')
    print('0. Salir')
    opcion = int(input('Elija una opción\n'))

    match opcion:
        case 1:
            cantidad = float(input('¿Cuánto ha recaudado hoy?\n'))
            recaudado.append(cantidad)

        case 2:
            for i, valor in enumerate(recaudado):
                print(f'{i + 1}º: {valor:.2f}€')

            opcion = int(input('¿Cuál quiere poner a 0?\n'))
            recaudado[opcion - 1] = 0
            print('¡Hecho!')

        case 3:
            print('Su recaudación por días es:')
            for i, valor in enumerate(recaudado):
                print(f'{i + 1}º: {valor:.2f}€')

        case 4:
            maximo = max(recaudado)
            print(f'El día que más ganaste fue: {maximo:.2f}€')
            print(f'Aparece: {recaudado.count(maximo)}')

        case 5:
            for i, valor in enumerate(recaudado):
                print(f'{i + 1}º: {valor:.2f}€')
            opcion = int(input('¿A qué día le sumo la cantidad?\n'))
            cantidad = float(input('¿Qué cantidad?\n'))
            recaudado[opcion - 1] += cantidad

        case 6:
            print(f'Total recaudado: {sum(recaudado):.2f}€')

        case 7:
            recaudado.sort(reverse=True)
            print(f'Lista ordenada: {recaudado:.2f}')

        case 8:
            if recaudado:
                print(f'Media diaria: {sum(recaudado) / len(recaudado):.2f}€')
            else:
                print('No hay datos')

        case 9:

            for valor in recaudado:
                if valor > 0:
                    alquilados += 1
            print(f'Porcentaje de ocupación: {alquilados / 30 * 100:.2f}%')

        case 10:
            ordenada = sorted(recaudado)
            menores = ordenada[:5]
            restantes = ordenada[5:]
            print(f'5 menores: {menores}')
            print(f'Restantes: {restantes}')

        case 0:
            print('Hasta pronto')
            break

        case _:
            print('Opción incorrecta')
