"""Escribir un programa que permita ingresar un numero entero n.
debe mostrar los primeros miltiplos de n
ejemplo n = 5

n x 1 = 5
n x 2 = 10
n x 3 = 15
n x 4 = 20
...
n x 10 = 50"""

from random import randint
la_tabla_del = randint(1, 10)
for numero in range(1, 11):
# PAra cada numero en el rango ==> [1,2,3,4,5,6,7,8,9,10]
   print(f"{la_tabla_del} x {numero} = {la_tabla_del * numero}")