# Creando diccionarios
empty_dict = {}
rae = {
    'bifronte': 'De dos frentes o dos caras',
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa',
}

population_can = {
    2015: 2_135_209,
    2016: 2_154_924,
    2017: 2_177_048,
    2018: 2_206_901,
    2019: 2_220_270,
}


# Conversión
# Para convertir otros tipos de datos en un diccionario podemos usar la función dict():
# Diccionario a partir de una lista de cadenas de texto
dict(['a1', 'b2'])
{'a': 1, 'b': 2}
# Diccionario a partir de una tupla de cadenas de texto
dict(('a1', 'b2'))
{'a': 1, 'b': 2}
# Diccionario a partir de una lista de listas
dict([['a', 1], ['b', 2]])
{'a': 1, 'b': 2}


# Operaciones con diccionarios
# Obtener un elemento
rae = {
    'bifronte': 'De dos frentes o dos caras ',
    'anarcoide': 'Que tiende al desorden ',
    'montuvio': 'Campesino de la costa',
}

print(rae['anarcoide'])

# Usando get()
# Existe una función muy útil para «superar» los posibles errores de acceso por claves
# inexistentes. Se trata de get() y su comportamiento es el siguiente:
# 1. Si la clave que buscamos existe, nos devuelve su valor.
# 2. Si la clave que buscamos no existe, nos devuelve None salvo que le indiquemos otro
# valor por defecto, pero en ninguno de los dos casos obtendremos un error.
rae = {
    'bifronte': 'De dos frentes o dos caras ',
    'anarcoide': 'Que tiende al desorden ',
    'montuvio': 'Campesino de la costa',
}

print(rae.get('bifronte'))
print(rae.get('programación', 'No encontrado'))
# Este segundo sirve para dar un mensaje en el caso de que no se encuentra


# Añadir o modificar un elemento
# Si la clave ya existía en el diccionario, se reemplaza el valor existente por el nuevo.
# Si la clave es nueva, se añade al diccionario con su valor. No vamos a obtener un
# error a diferencia de las listas.
