"""
Escribir un programa que lea números enteros 
hasta que de la suma de estos sea mayor que 100, 
y muestre la cantidd de numeros ingresados.

random 0.0 ... 0.99999999999

"""

import random

numero = random.randint(1, 10)
contador = 0
suma = 0

while suma <= 100:
    
    contador += 1
    suma += numero
    print(f"El numero es: {numero} y la suma es: {suma} y la cantidad de numeros es: {contador}")
    numero = random.randint(1, 10)
print(f"Cantidad de numeros: {contador}")




