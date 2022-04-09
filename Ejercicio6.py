"""EJERCICIO 6.- Calcular el área y el perímetro de un Rectángulo

En el siguiente ejercicio se solicita calcular el área y el perímetro de un
Rectángulo, para ello deberemos crearlas siguientes variables:

alto (int)

ancho (int)"""
 
alto=int(input("Dime el ancho: "))
ancho=int(input("Dime el alto: "))
perimetro = 2*ancho + 2*alto
area = ancho * alto
print("Resultado: Area=%.2f Perimetro=%.2f" % (area,perimetro))