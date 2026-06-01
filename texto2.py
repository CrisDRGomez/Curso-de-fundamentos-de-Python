# En esta clase vamos a aprender sobre índices en cadenas de texto. En Python, cada carácter en una cadena de texto tiene un índice asociado, 
# que comienza en 0 para el primer carácter, 1 para el segundo, y así sucesivamente. 

print("""\nEn esta clase vamos a aprender sobre índices en cadenas de texto. En Python, cada carácter en una cadena de texto tiene un índice asociado, 
que comienza en 0 para el primer carácter, 1 para el segundo, y así sucesivamente.\n""")

# Por ejemplo, si tenemos la cadena de texto "Este es un texto", los índices serán:
print ("Por ejemplo, si tenemos la cadena de texto\n")

texto = "Este es un texto"

print(""" "" """, texto, """ "" """) # Esto imprimirá "Este es un texto"


# Sus índices serían:
# E  s  t  e     e  s     u  n     t  e  x  t  o
# 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
print("\nSus índices serían:\n")
print(" E    s    t    e         e    s         u    n          t     e     x     t     o")
print("[0]  [1]  [2]  [3]  [4]  [5]  [6]  [7]  [8]  [9]  [10]  [11]  [12]  [13]  [14]  [15]\n")

# Podemos acceder a cada carácter de la cadena utilizando su índice considerando que los espacios también cuentan como caracteres.

# Al acceder a cada carácter tendrás de resultado en la consola el carácter correspondiente 
# al índice que has utilizado, por ejemplo, al acceder al índice [0] obtendrás el primer carácter 
# de la cadena de texto, que en este caso es "E".

print("""Podemos acceder a cada carácter de la cadena utilizando su índice considerando que los espacios también cuentan como caracteres. 

Al acceder a cada carácter tendrás de resultado en la consola el carácter correspondiente 
al índice que has utilizado, por ejemplo, al acceder al índice [0] obtendrás el primer carácter 
de la cadena de texto, que en este caso es "E".

Para ello usaremos el script para imprimir cada carácter según su índice:

"print(texto[índice])"\n""")

print("================================================================================================")

print("\nEjemplo de acceso con índices positivos:\n")

print("""Cáracter  Resultado\n""")
print("   " + texto[0] + "      Primer espacio [0] del índice de la cadena de texto") # imprime "E"
print("   " + texto[1] + "      Segundo espacio [1] del índice de la cadena de texto") # imprime "s"
print("   " + texto[2] + "      Tercer espacio [2] del índice de la cadena de texto") # imprime "t"
print("   " + texto[3] + "      Cuarto espacio [3] del índice de la cadena de texto") # imprime "e"
print("   " + texto[4] + "      Quinto espacio [4] del índice de la cadena de texto") # imprime "un espacio"
print("   " + texto[5] + "      Sexto espacio [5] del índice de la cadena de texto") # imprime "e"
print("   " + texto[6] + "      Séptimo espacio [6] del índice de la cadena de texto") # imprime "s"
print("   " + texto[7] + "      Octavo espacio [7] del índice de la cadena de texto") # imprime "un espacio"
print("   " + texto[8] + "      Noveno espacio [8] del índice de la cadena de texto") # imprime "u"
print("   " + texto[9] + "      Décimo espacio [9] del índice de la cadena de texto") # imprime "n"
print("   " + texto[10] + "      Undécimo espacio [10] del índice de la cadena de texto") # imprime "un espacio"
print("   " + texto[11] + "      Duodécimo espacio [11] del índice de la cadena de texto") # imprime "t"
print("   " + texto[12] + "      Decimotercer espacio [12] del índice de la cadena de texto") # imprime "e"
print("   " + texto[13] + "      Decimocuarto espacio [13] del índice de la cadena de texto") # imprime "x"
print("   " + texto[14] + "      Decimoquinto espacio [14] del índice de la cadena de texto") # imprime "t"
print("   " + texto[15] + "      Decimosexto espacio [15] del índice de la cadena de texto") # imprime "o"

# Esto ocurre porque los indices son positivos pero ¿Qué pasa si usamos índices negativos?
print("\nEsto ocurre porque los indices son positivos pero ¿Qué pasa si usamos índices negativos?\n")

print("================================================================================================")
# También podemos usar índices negativos para acceder a los caracteres desde el final de la cadena. Por ejemplo:
print("\nEjemplo de acceso con índices negativos:\n")

print("""Cáracter  Resultado\n""")
print("   " + texto[-1] + "      Último espacio [-1] del índice de la cadena de texto") # o
print("   " + texto[-2] + "      Penúltimo espacio [-2] del índice de la cadena de texto") # t    
print("   " + texto[-3] + "      Antepenúltimo espacio [-3] del índice de la cadena de texto") # x
print("   " + texto[-4] + "      Cuarto desde el final [-4] del índice de la cadena de texto") # e
print("   " + texto[-5] + "      Quinto desde el final [-5] del índice de la cadena de texto") # t
print("   " + texto[-6] + "      Sexto desde el final [-6] del índice de la cadena de texto") # (espacio)
print("   " + texto[-7] + "      Séptimo desde el final [-7] del índice de la cadena de texto") # n
print("   " + texto[-8] + "      Octavo desde el final [-8] del índice de la cadena de texto") # u
print("   " + texto[-9] + "      Noveno desde el final [-9] del índice de la cadena de texto") # (espacio)
print("   " + texto[-10] + "      Décimo desde el final [-10] del índice de la cadena de texto") # s
print("   " + texto[-11] + "      Undécimo desde el final [-11] del índice de la cadena de texto") # e
print("   " + texto[-12] + "      Duodécimo desde el final [-12] del índice de la cadena de texto") # (espacio)
print("   " + texto[-13] + "      Decimotercer desde el final [-13] del índice de la cadena de texto") # e
print("   " + texto[-14] + "      Decimocuarto desde el final [-14] del índice de la cadena de texto") # t
print("   " + texto[-15] + "      Decimoquinto desde el final [-15] del índice de la cadena de texto") # s
print("   " + texto[-16] + "      Decimosexto desde el final [-16] del índice de la cadena de texto") # E

# Es importante tener en cuenta que si intentamos acceder a un índice que está fuera del rango de la cadena, obtendremos un error. Por ejemplo:
print("\nEs importante tener en cuenta que si intentamos acceder a un índice que está fuera del rango de la cadena, obtendremos un error.\n")

print("""================================================================================================\n""")
print("""*El ejemplo de intentar acceder a un índice fuera del rango de la cadena esta comentado para poder continuar con el resto de las notas sin interrupciones, ya que los
"errores" detienen la ejecución del programa y por lo tanto no se ejecutará el resto del código, descomenta la línea de código 93 para ver el error.*\n""")
print("""================================================================================================\n""")

#print(texto[16]) # Esto generará un error porque el índice 16 no existe en la cadena "Este es un texto".

# En resumen, los índices en cadenas de texto nos permiten acceder a cada carácter individualmente, ya sea desde el principio o desde el final 
# de la cadena. Es una herramienta fundamental para manipular y trabajar con texto en Python. 
print("""\nEn resumen, los índices en cadenas de texto nos permiten acceder a cada carácter individualmente, ya sea desde el principio o desde el final
de la cadena. Es una herramienta fundamental para manipular y trabajar con texto en Python.\n\n""")

#El Slicing en Python es una técnica que nos permite obtener una parte específica de una secuencia, como una cadena de texto, una lista o una tupla.
#El slicing se realiza utilizando la sintaxis [inicio:fin:paso], donde "inicio" es el índice de inicio, "fin" es el índice de fin (no incluido) y "paso"
#es el número de elementos a saltar. Si omitimos alguno de los parámetros, se asume un valor predeterminado. Por ejemplo:

#Slicing
print("""================================================================================================""")
print("""El Slicing""")
print("""================================================================================================\n""")
print("""\nEl Slicing en Python es una técnica que nos permite obtener una parte específica de una secuencia, como una cadena de texto, una lista o una tupla.

El slicing se realiza utilizando la sintaxis [inicio:fin:paso], donde "inicio" es el índice donde queremos comenzar (puede ser cero [0] u otro valor e incluso estar vacío), 
"fin" es el índice de fin (puede ser cualquier valor dentro de la longitud de la cadena y puede estar vacío) y "paso" es el número de elementos a saltar. 

Si omitimos alguno de los parámetros, se asume un valor predeterminado. Por ejemplo:\n""")
print("""================================================================================================\n""")

# Obtener una subcadena de texto con slicing
subcadena = texto[0:10] # Esto obtendrá los caracteres desde el índice 0 hasta el índice 9 (no incluido)
print("Ejemplo de obtener una subcadena de texto con slicing con un índice específico:\n")
print("Al tener la siguiente subcadena de texto:\n\n subcadena = texto[0:10]\n\n el resultado será:\n")
print(subcadena + "\n") # Esto imprimirá "Este es un "


# Obtener una subcadena desde el inicio hasta un índice específico
subcadena = texto[:4] # Esto obtendrá los caracteres desde el inicio hasta el índice 3 (no incluido)
print("Ejemplo de obtener una subcadena desde un valor predeterminado hasta un índice específico:\n")
print("Al tener la siguiente subcadena de texto:\n\n subcadena = texto[:4]\n\n el resultado será:\n")
print(subcadena + "\n") # Esto imprimirá "Este"

# Obtener una subcadena desde un índice específico hasta el final
subcadena = texto[5:] # Esto obtendrá los caracteres desde el índice 5 hasta el final de la cadena
print("Ejemplo de obtener una subcadena desde un índice específico hasta un valor predeterminado:\n")
print("Al tener la siguiente subcadena de texto:\n\n subcadena = texto[5:]\n\n el resultado será:\n")
print(subcadena + "\n") # Esto imprimirá "es un texto"

# Obtener una subcadena con un paso específico
subcadena = texto[0:16:2]# Esto obtendrá los caracteres desde el índice 0 hasta el índice 15 (no incluido) con un paso de 2
print("Ejemplo de obtener una subcadena con un paso específico:\n")
print("Al tener la siguiente subcadena de texto:\n\n subcadena = texto[0:16:2]\n\n el resultado será:\n")
print(subcadena + "\n") # Esto imprimirá "Et s n eto"

# También podemos usar índices negativos en el slicing. Por ejemplo:
print("También podemos usar índices negativos en el slicing. Por ejemplo:\n")
# Obtener una subcadena desde el final hasta un índice específico
subcadena = texto[-5:] # Esto obtendrá los últimos 5 caracteres de la cadena
print("Al tener la siguiente subcadena de texto:\n\n subcadena = texto[-5:]\n\n el resultado será:\n")
print(subcadena) # Esto imprimirá "texto"

# Obtener una subcadena desde un índice específico hasta el final
subcadena = texto[:-5] # Esto obtendrá los caracteres desde el inicio hasta los últimos 5 caracteres (no incluido)
print("Al tener la siguiente subcadena de texto:\n\n subcadena = texto[:-5]\n\n el resultado será:\n")
print(subcadena) # Esto imprimirá "Este es un "


#Ejemplo
curso = "Este es un curso de Javascript"
print(curso.replace("Javascript", "Python")) # Esto reemplazará "Javascript" por "Python" en la cadena de texto 