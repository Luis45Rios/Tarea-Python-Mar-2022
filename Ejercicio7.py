"""EJERCICIO 7.- Realiza un programa que pida dos números ‘a’ y ‘b’ 
e indique si su suma es positiva, negativa o cero."""

a= int(input("Ponme un número por favor: "))
b= int(input("Dame otro numero por favor: "))
c = (a+b)

if a < b:
    print("Esta suma es negativa")
elif a + b > 0:
    print("Esta suma es positiva")
if a + b == 0:
    print("Esta suma no es negativa, ni positiva")
print(c)