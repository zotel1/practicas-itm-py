"""
Escribir un programa que permita validar la nota de un examen.
Se espera que la nota que el usuario ingrese sea un número comprendido entre 0 y 10.
La misma debe ser ingresada tantas veces como sea necesario 
hasta que quede comprendida dentro del rango indicado.

Las notas 1 y 3 no usan nunca.
La nota 0 se reserva para los ausentes.
Las notas válidas pueden ser un 2 o un valor entre 4 y 10.
"""

"""nota = int(input("Nota: "))
#Expresado por extension
#while (nota not in (2,4,5,6,7,8,9,10)):

#Expresado por Comprension
while (nota not in (2,range(4,11))):

    nota = int(input("Nota: "))

for x in (2, range(4,11)):
    print(x)
nota = int(input("Nota: ))
"""
print("-"*125)

z = tuple(range(4, 11))
z += (2,)

nota = int(input("Nota: "))
while(nota not in z):
    nota = int(input("Nota: "))