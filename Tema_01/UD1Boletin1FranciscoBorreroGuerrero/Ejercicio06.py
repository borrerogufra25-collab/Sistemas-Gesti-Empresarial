import random

# 6) Añadir al ejercicio anterior que si está entre 11 y 20,
# muestre otro mensaje diferente y si está entre 21 y 30 otro mensaje.

num = random.randint(0, 30)

print(num)
if num >= 0 and num <= 10:
    print("El número está entre el 0 y el 10")
elif num >= 11 and num <= 20:
    print("El número está entre el 11 y el 20")
elif num >= 21 and num <= 30:
    print("El número está entre el 21 y el 30")
else:
    print("El número está fuera")
