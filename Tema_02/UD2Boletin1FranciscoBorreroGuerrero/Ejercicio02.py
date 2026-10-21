# 2. Crear un programa que explique las distintas funcionalidades de Python usando listas. Puedes empezar con
# las típicas CRUD y hacerlo con una lista rellena directamente. Ejemplo: buscar, insertar al final o en una
# posición concreta, borrar, distintas formas de eliminar... Puedes seguir el orden del archivo de teoría.

# 1. Crear
frutas = ["manzana", "plátano", "pera", "melón"]
print("Lista inicial:", frutas)

# 2. Leer y buscar
print("Primer elemento:", frutas[0])
print("Último elemento:", frutas[-1])
print("¿Existe 'plátano' en la lista?:", "plátano" in frutas)
print("Posición de 'pera':", frutas.index("pera"))

# 3. Actualizar
frutas[1] = "plátano"  # Cambiar el valor del índice 1
frutas.append("uva")  # Añadir al final
frutas.insert(1, "mango")  # Insertar en una posición específica (índice 1)
print("Después de los cambios:", frutas)

# 4. Borrar
frutas.remove("manzana")  # 1. Eliminar por valor
print("Después de borrar ('manzana'):", frutas)

eliminado = frutas.pop(2)  # 2. Eliminar por índice guardando el valor
print(f"Tras pop(2) (se borró '{eliminado}'):", frutas)

del frutas[0]  # 3. Eliminar por índice directo con 'del'
print("Tras del frutas[0]:", frutas)

# 5. Ordenar
frutas.sort()  # Ordenar alfabéticamente
print("Lista ordenada:", frutas)

frutas.clear()  # Vaciar la lista por completo
print("Lista vacía:", frutas)
