#=====================================
# Números
#=====================================

x = 1
y = 2.5
z = 1j

print(type(x))
print(type(y))
print(type(z))

#Los númweros pueden ser positivos o negativos, dependiendo de su valor. Un número positivo es mayor que cero, mientras que un número negativo es menor que cero.

positivo = 5.5 
negativo = -3.5

#Los números imaginarios son aquellos que se representan con la letra "j" en Python. Estos números se utilizan para representar cantidades que no pueden ser 
# expresadas como números reales, como la raíz cuadrada de un número negativo.   

imaginario = 2 + 3j
imaginario2 = 4 - 5j


#=====================================
# Casteo/Conversión de tipos de datos
#=====================================

#El casteo o conversión de tipos de datos es el proceso de convertir un valor de un tipo de dato a otro. En Python, esto se puede hacer utilizando las funciones 
#integradas como int(), float(), str(), etc.    
xf = float(x)
print(type(xf))
print(xf)

ye = int(y)
print(type(ye))
print(ye)

entero = 5
flotante = 5.5

enteroComplejo = complex(entero)
flotanteComplejo = complex(flotante)

print(enteroComplejo) # Salida: (5+0j)
print(type(enteroComplejo)) # Salida: <class 'complex'>

print(flotanteComplejo) # Salida: (5.5+0j)
print(type(flotanteComplejo)) # Salida: <class 'complex'>

#=====================================
# Números aleatorios
#=====================================

import random

print(random.randint(1, 10)) # Genera un número entero aleatorio entre 1 y 9
print(random.uniform(1.0, 10.0)) # Genera un número flotante aleatorio entre 1.0 y 9.0