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
