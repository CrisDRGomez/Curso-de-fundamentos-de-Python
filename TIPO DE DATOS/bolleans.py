v = True
f = False

print(v) # Salida: True
print(f) # Salida: False

print(5 >3) # Salida: True
print(3 > 5) # Salida: False

print(type(v)) # Salida: <class 'bool'>
print(type(f)) # Salida: <class 'bool'>

print(bool("Hola Mundo"))
print(bool("")) # Salida: False - las cadenas vacías se consideran False

#True
print(bool("abc")) # Salida: "abc" - cualquier cadena no vacía se considera True
print(bool(42)) # Cualquier número distinto de cero se considera True
print(bool(123)) # Cualquier número distinto de cero se considera True
print(bool(-1)) # Cualquier número distinto de cero se considera True
print(bool("Manzana" + "Pera")) # Salida: "ManzanaPera" - la concatenación de dos cadenas no vacías se considera True
print(bool([1, 2, 3])) # Lista no vacía
print(bool((1, 2, 3))) # Tupla no vacía

#false
print(bool("")) # Cadena vacía
print(bool(0)) # Cero
print(bool(0.0)) # Cero en punto flotante
print(bool([])) # Lista vacía
print(bool(())) # Tupla vacía   
print(bool({})) # Diccionario vacío
print(bool(set())) # Conjunto vacío
print(bool(None)) # El valor None se considera False

x = 123.5
print(isinstance(x, int)) # Salida: True - x es un entero