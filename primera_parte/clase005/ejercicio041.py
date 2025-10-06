"""
Escribir un programa que lea numeros enteros hasta que se ingrese un 0 y muestre el maximo.
"""

# Antes (para todos)
maximo = float('-inf')
minimo = float('inf')
numero = int(input("Ingrese un numero: "))
hay_datos = False
while numero != 0:
    hay_datos = True
    #Durante (para cada dato)
    #numero = int(input("numero: "))
    if numero > maximo:
        maximo = numero

    if numero < minimo:
        minimo = numero
        #Leer un nuevo numero
    numero = int(input("Ingrese un numero: "))


#Despues
if hay_datos:
    print(f"maximo: {maximo}")
    print(f"minimo: {minimo}")
else:
    print("No se ingresaron datos")