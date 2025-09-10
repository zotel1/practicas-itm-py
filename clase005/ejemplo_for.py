"""
Leer 10 numeros y realizar la suma"""

# ANTES
suma = 0
cantidad = 10
for contador in range(1, cantidad+1):
    # DURANTE
    numero = int(input(f"Ingrese el {contador} de {cantidad} numeros: : "))
    suma += numero
# DESPUES
print(f"La suma es: {suma}")