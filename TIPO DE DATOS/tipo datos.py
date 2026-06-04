#============================
#Texto
#============================

comillasSimples = 'Este es un texto con comillas simples'
comillasDobles = "Este es un texto con comillas dobles"
comillasSimplesYDobles = 'Este es un texto con comillas simples y "comillas dobles"'
comillasTribles = '''Este es un texto con comillas triples,
que permite escribir en varias líneas, y también permite usar 'comillas simples' y "comillas dobles" sin problemas.'''

print(comillasSimples)
print(comillasDobles)
print(comillasSimplesYDobles)
print(comillasTribles)

#============================
#Números
#============================

#Números enteros

a = 1

print(a)

#Números decimales

b = 3.14

print(b)

#Números complejos

c = 2 + 3j

print(c)


#============================
#Listas
#============================

#Las listas son mutables, lo que significa que se pueden modificar después de su creación. Se definen utilizando corchetes [] y los elementos se separan por comas.

lista = [0, 1, 2, 3, 4, 5]


#============================
#Tuplas
#============================

#Las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación. Se definen utilizando paréntesis () y los elementos se separan por comas.

tupla = ("a", "b", "c", "d", "e")

#============================
#Diccionarios
#============================

#Los diccionarios son estructuras de datos que almacenan pares de clave-valor. Se definen utilizando llaves {} y los elementos se separan por comas. 
#Cada par de clave-valor se separa por dos puntos :.

diccionario = {
    "nombre": "Juan", 
    "edad": 30, 
    "ciudad": "Madrid"
    }    

#============================
#Conjuntos
#============================

#Los conjuntos son colecciones de elementos únicos y no ordenados. Se definen utilizando llaves {} o la función set().

conjunto = {1, 1, 2, 2, 3}
print(conjunto) # Salida: {1, 2, 3} - los elementos duplicados se eliminan automáticamente 

#============================
#Booleanos
#============================

#Los booleanos son un tipo de dato que representa dos valores posibles: True (verdadero) y False (falso). Se utilizan 
#para realizar operaciones lógicas y tomar decisiones en el código.    

booleanoVerdadero = True
booleanoFalso = False