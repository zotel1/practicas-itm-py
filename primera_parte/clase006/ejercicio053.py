"""
Escribir un orograma que permita ingresar nombre y edad de un grupo de personas
(para cada una, nombre y edad). La carga termina cuando en el nombre de la persona 
se ingresa un asterisco ('*'). Mostrar al final cómo se llama la persona más joven.
"""

nombre = str(input("Ingrese un nombre: "))
minima_edad = float("inf")

while(nombre != "*"):
    edad = int(input("Ingrese su edad: "))

    if (edad <= minima_edad):
        minima_edad = edad
        minimo_nombre = nombre

    nombre = str(input("Ingrese su nombre: "))

print(f"El menor es: {minimo_nombre}")
    