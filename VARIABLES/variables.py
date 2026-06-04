#=========================================================
# VARIABLES
#=========================================================

#Las variables son espacios en la memoria de la computadora que se 
#utilizan para almacenar datos. En Python, no es necesario declarar 
#el tipo de variable, ya que el lenguaje lo infiere automáticamente.

#Para crear una variable, simplemente asignamos un valor a un nombre utilizando el operador de asignación (=).

x = "Esta es una variable de tipo string"
print(x)

#Una variable puede soberescribirse con un nuevo valor, incluso si es de un tipo diferente.  

x = "Acá estoy escribiendo otra cosa"
print(x)

#Se puede escribir una variable en minúscula o mayúscula, pero es importante ser consistente para evitar confusiones.

mivariable = "Esta es una variable en minúscula"
MiVariable = "Esta es una variable en mayúscula"
MIVARIABLE = "Esta es una variable en mayúscula completa" #Se utiliza Mayuscula completa para nombrar constantes, es decir, valores que no cambian a lo largo del programa. 

print(mivariable)
print(MiVariable)   

#También podemos nombrarla con guiónes bajos para mejorar la legibilidad.

mi_variable = "Esta es una variable con guión bajo"

print(mi_variable)

_mi_variable = "Esta es una variable con guión bajo al inicio" #El guión bajo al inicio de una variable se utiliza para indicar que es una variable privada, es decir, que no 
#debe ser accedida desde fuera de la clase o módulo en el que se define. Sin embargo, esto es solo una convención y no impide realmente el acceso a la variable desde fuera 
#de la clase o módulo.  

print(_mi_variable)

#Reglas para nombrar variables en Python:

#"No se pueden usar espacios en los nombres de las variables, pero se pueden usar guiones bajos para separar palabras."
#"No se pueden usar caracteres especiales en los nombres de las variables, excepto el guión bajo."
#"No se pueden usar palabras reservadas de Python como nombres de variables, como 'if', 'for', 'while', etc."
#"No se pueden usar números al inicio de los nombres de las variables, pero sí pueden contener números después del primer carácter."

#===========================================================================================================
# Nomenclatura de variables
#===========================================================================================================

#Camel Case: En esta convención, cada palabra en el nombre de la variable comienza con una letra mayúscula, excepto la primera 
#palabra que comienza con una letra minúscula. Ejemplo: miVariable, nombreCompleto.    

#Snake Case: En esta convención, las palabras en el nombre de la variable están separadas por guiones bajos. Ejemplo: mi_variable, nombre_completo.

#Pascal Case: En esta convención, cada palabra en el nombre de la variable comienza con una letra mayúscula, incluyendo la primera palabra. 
#Ejemplo: MiVariable, NombreCompleto.    