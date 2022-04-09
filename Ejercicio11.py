"""EJERCICIO 11.-Escribir un programa que lea un año indicar si es bisiesto. 
Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, 
excepto que también sea divisible por 400."""

"""def año_bisiesto(anio: int) -> int:
     return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)
print(año_bisiesto(2022))"""
def es_bisiesto(anio: int) -> bool:
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


print(es_bisiesto(2000))

inicio = 2000
fin = 2022
print(f"Imprimiendo años bisiestos del {inicio} al {fin}")
# Le sumamos uno al fin, porque range no incluye el límite superior
for anio in range(inicio, fin+1):
    if es_bisiesto(anio):
        print(anio, end=", ")
