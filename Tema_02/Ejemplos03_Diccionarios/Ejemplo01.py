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
# Para añadir o modificar basta con hacer referencia a la clave y asignarle un valor.
rae = {
    'bifronte': 'De dos frentes o dos caras',
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa',
}

# La clave 'enjuiciar' es nueva, así que se añade al diccionario
rae['enjuiciar'] = 'Someter una cuestión a examen, discusión y juicio'
print(rae)

# La clave 'enjuiciar' ya existe, así que se reemplaza su valor por el nuevo
rae['enjuiciar'] = 'Instruir, juzgar o sentenciar una causa'
print(rae)


# Creando desde vacío
# Un patrón muy habitual es partir de un diccionario vacío e ir añadiendo elementos
# poco a poco. Aquí las claves son las vocales y los valores son sus posiciones.
# Usamos enumerate() con start=1 para que la cuenta empiece en 1.
VOWELS = 'aeiou'

enum_vowels = {}
for i, vowel in enumerate(VOWELS, start=1):
    enum_vowels[vowel] = i

print(enum_vowels)  # {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}


# Pertenencia de una clave
# La forma pitónica de comprobar si una clave existe es el operador in (o not in).
# Siempre devuelve un booleano: True o False.
print('bifronte' in rae)  # True
print('almohada' in rae)  # False
print('montuvio' not in rae)  # False


# Obtener todos los elementos
# Python ofrece tres funciones para obtener los elementos de un diccionario:
# keys() (claves), values() (valores) e items() (pares clave-valor).
print(rae.keys())
print(rae.values())
# items() devuelve los pares como tuplas: (clave, valor)
print(rae.items())
# dict_items([('bifronte', 'De dos frentes o dos caras'), ('anarcoide', ...), ...])


# Longitud de un diccionario
# len() devuelve el número de pares clave-valor.
print(len(rae))  # 4


# Iterar sobre un diccionario
# Hay tres maneras de iterar, según lo que queramos recorrer.

# Iterar sobre claves
for word in rae.keys():
    print(word)

# Iterar sobre valores
for meaning in rae.values():
    print(meaning)

# Iterar sobre clave-valor (usamos f-strings para formatear el texto)
for word, meaning in rae.items():
    print(f'{word}: {meaning}')


# Combinar diccionarios
# Se basa en dos premisas:
# 1. Si la clave no existe, se añade con su valor.
# 2. Si la clave ya existe, se queda el valor del «último» diccionario (el más a la derecha).
rae1 = {
    'bifronte': 'De dos frentes o dos caras',
    'enjuiciar': 'Someter una cuestión a examen, discusión y juicio',
}

rae2 = {
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa',
    'enjuiciar': 'Instruir, juzgar o sentenciar una causa',
}

# Sin modificar los originales: operador **
print({**rae1, **rae2})

# Sin modificar los originales (Python 3.9 o superior): operador |
print(rae1 | rae2)

# Modificando el original: update() actualiza rae1 con el contenido de rae2
rae1.update(rae2)
print(rae1)

# El orden importa: con {**rae2, **rae1} ganaría el valor de rae1 en 'enjuiciar'


# Borrar elementos
# Por su clave: sentencia del
rae = {
    'bifronte': 'De dos frentes o dos caras',
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa',
}

del rae['bifronte']
print(rae)

# Por su clave, con extracción: pop() borra el elemento y devuelve su valor
# (viene a ser una combinación de get() + del)
rae = {
    'bifronte': 'De dos frentes o dos caras',
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa',
}

print(rae.pop('anarcoide'))  # Que tiende al desorden
print(rae)  # {'bifronte': ..., 'montuvio': ...}

# Cuidado: si la clave que queremos extraer con pop() no existe, obtenemos un error
# rae.pop('bucle')  # KeyError: 'bucle'

# Borrado completo, opción 1: clear()
rae = {
    'bifronte': 'De dos frentes o dos caras',
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa',
}

rae.clear()
print(rae)

# Borrado completo, opción 2: reinicializar a vacío con {}
rae = {
    'bifronte': 'De dos frentes o dos caras',
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa',
}

rae = {}
print(rae)  # No recomendable


# Cuidado con las copias
# Los diccionarios son mutables, así que si hacemos copy_rae = original_rae
# ambas variables apuntan al MISMO diccionario y un cambio se refleja en las dos.
original_rae = {
    'bifronte': 'De dos frentes o dos caras',
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa',
}

copy_rae = original_rae
original_rae['bifronte'] = 'bla bla bla'

print(original_rae)  # 'bifronte': 'bla bla bla'
print(copy_rae)  # 'bifronte': 'bla bla bla'  <- también ha cambiado

# Solución: hacer una «copia dura» con copy(), que crea un diccionario independiente
original_rae = {
    'bifronte': 'De dos frentes o dos caras',
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa',
}

copy_rae = original_rae.copy()
original_rae['bifronte'] = 'bla bla bla'

print(original_rae)  # 'bifronte': 'bla bla bla'
print(copy_rae)  # 'bifronte': 'De dos frentes o dos caras'  <- no ha cambiado

# Si el diccionario contiene elementos mutables hay que usar deepcopy(),
# del módulo copy de la librería estándar
from copy import deepcopy

copy_rae = deepcopy(original_rae)


# Diccionarios por comprensión
# Igual que las listas por comprensión, pero usando llaves {}.
# Aquí las claves son palabras y los valores son sus longitudes.
words = ('sun', 'space', 'rocket', 'earth')

words_length = {word: len(word) for word in words}
print(words_length)  # {'sun': 3, 'space': 5, 'rocket': 6, 'earth': 5}

# También podemos añadir condiciones.
# Aquí solo incluimos las palabras que no empiezan por vocal.
words_length = {w: len(w) for w in words if w[0] not in 'aeiou'}
print(words_length)  # {'sun': 3, 'space': 5, 'rocket': 6}


# Objetos «hashables»
# La única restricción para las claves de un diccionario es que sean «hashables»:
# que se les pueda asignar un valor hash que no cambie durante toda su vida.
# La función hash() devuelve ese valor (un entero).
print(hash(999))  # 999
print(hash(3.14))  # 322818021289917443
print(hash('hello'))  # varía en cada ejecución (para cadenas)
print(hash(('a', 'b', 'c')))  # varía en cada ejecución (por contener cadenas)

# Para ser «hashable» un objeto debe ser inmutable. Una lista no lo es:
# hash(['a', 'b', 'c'])  # TypeError: unhashable type: 'list'
# Por eso las claves de un diccionario solo pueden ser objetos inmutables.

# hash() realmente llama al método mágico __hash__() del objeto
print(hash('spiderman') == 'spiderman'.__hash__())  # True
