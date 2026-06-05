# Operadores Aritméticos

x = 5
y = 10

# Suma +
print("Suma", x + y) # Salida: 15

# Resta -
print("Resta", x - y) # Salida: -5

# Multiplicación *
print("Multiplicación", x * y) # Salida: 50

# División /
print("División", y / x) # Salida: 2.0 siempre devuelve un número de punto flotante, incluso si ambos operandos son enteros y el resultado es un número entero.

# División entera //
print("División entera", y // x) # Salida: 2

# Módulo %
print("Módulo", y % x) # Salida: 0

# Exponenciación **
print("Exponenciación", y ** x) # Salida: 100000

#Saber si un numero es par

numero = 8
es_par = numero % 2 == 0
print("¿El número es par?", es_par) # Salida: True

# Presedencia de operadores

# 1. Paréntesis ()
# 2. Exponenciación **
# 3. Multiplicación *, División /, División entera //, Módulo %
# 4. Suma +, Resta -
resultado = 2 + 3 * 4 ** 2
print("Resultado sin paréntesis", resultado) # Salida: 50

# Con paréntesis
resultado = (2 + 3) * 4 ** 2
print("Resultado con paréntesis", resultado) # Salida: 80
