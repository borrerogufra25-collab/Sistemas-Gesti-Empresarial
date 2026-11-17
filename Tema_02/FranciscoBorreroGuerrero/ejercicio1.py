tapa_reina = ("Ensaladilla Rusa", 4.50, 5)

nombre, precio, tiempo = tapa_reina

print(f"La tapa se llama: {nombre}")
print(f"El precio es: {precio}€")
print(f"Se tarda en preparar: {tiempo} minutos")


nombreTroceado = tuple(tapa_reina[:1])
precioTroceado = tuple(tapa_reina[1:2])

print(nombreTroceado)
print(precioTroceado)
