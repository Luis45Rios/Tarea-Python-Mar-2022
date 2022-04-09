"""EJERCICIO 10.- Escribe un programa que pida un nombre de usuario y una contraseña 
y si se ha introducido “pepe” y “passwd#” se indica “Has entrado al sistema”, 
sino se da un error."""

usuario = "Pepe"
clave = 0

while usuario != "Pepe" or clave != 12345:
    usuario = input("Nombre de usuario: ")
    clave = int(input("Ingresa la clave: "))

print("Bienvenido al sistema!!!")
