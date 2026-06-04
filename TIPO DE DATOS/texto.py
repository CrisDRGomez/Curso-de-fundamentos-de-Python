print("hola 'mundo'")

ingles = "I'm learning Python"

multiplesLineas = """Esto es un texto
que se extiende en varias líneas, y también permite usar 'comillas simples' y "comillas dobles" 

sin problemas."""

print(ingles)
print(multiplesLineas)

palabra = "Murciélago"
print(len(palabra)) # Salida: 10

texto = "Este curso es de fundamentos de python"
estaIncluida = "fundamentos" in texto
noEstaIncluida = "java" not in texto

print(estaIncluida) # Salida: True
print(noEstaIncluida) # Salida: True

#=====================================
# Formateo de cadenas
#=====================================

mayuscula = texto.upper()
print(mayuscula) # Salida: ESTE CURSO ES DE FUNDAMENTOS DE PYTHON

minuscula = texto.lower()
print(minuscula) # Salida: este curso es de fundamentos de python

texto2 = texto.upper()
texto2 = texto2.lower()
print(texto2) # Salida: este curso es de fundamentos de python

espacios = "   Hola mundo   "
sinEspacios = espacios.strip()
print(sinEspacios) # Salida: "Hola mundo"