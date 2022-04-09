"""EJERCICIO 13.- Pedir un número por teclado y mostrar la tabla de multiplicar"""
lista = []

i = 0

salir = False

while not salir:

    numero = int(input("Introduzca un numero: "))
    if numero != 0:        
        for i in range (0,11):
            resultado = i * numero
            i = i + 1
            lista.append(resultado)
        print(lista)
    else:
        print("Adios")
        salir = True