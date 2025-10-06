"""
generar 10000 numeros y mostrar el mayor y cuantas repeticiones tiene
"""

from random import randint

CANTIDAD = 50
maximo = -float('inf')
cantidad_maximos = 0
los_numeros = "Numeros: "
for x in range(CANTIDAD):
    numero = randint(1, 15)
    los_numeros += f'{numero} '
    if (numero > maximo):
        maximo = numero
        cantidad_maximos = 0
    elif (numero == maximo):
        cantidad_maximos += 1
print(los_numeros)
print(f"Maximo: {maximo} Se repite: {cantidad_maximos}")