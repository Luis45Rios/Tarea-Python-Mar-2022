"""EJERCICIO 14.- Crea una aplicación que pida un número y calcule su factorial 
(El factorial de un número es el producto de todos los enteros entre 1 y el propio número y 
se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120"""
y = input("Escriba un número: ")
x = int(y)
count = 1
z = 1
while z <= x:
    count = count * z
    z = z + 1
print(count)