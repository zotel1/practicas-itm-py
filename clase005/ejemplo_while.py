"""
Leer numeros hasta que se ingrese un cero. Mostrar la suma

lista1 ==> 1,2,3,5,4,6,7,8,9,6,4,3,2,4,5,7
lista1 ==> 1,2,3,5,4,6,7,8,9,6,4,3,2,4,5,7
lista1 ==> 1,2, 0
lista1 ==> 0
"""
# ANTES
suma = 0
numero = int(input("Ingrese un numero: "))
while numero != 0:

    ## DURANTE
    suma += numero
    numero = int(input("Ingrese un numero: "))

    #DESPUES
print(f"La suma es {suma}")