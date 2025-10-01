"""
Crea un diccionario en el cual las llaves sean números enteros y los valores sean
sus cuadrados. Haz esto para n numeros.
"""






def obtener_decc(n):
    return { x:x**2 for x in range(n)}


def obtener_tupla(n):
    return tuple( (x,x**2) for x in range(n))

def obtener_str(cantidad:int)->str:
    
    """
    List comprehension con join
    """
    return '~-~'.join([f"{numero}:{numero**2}" for numero in range(cantidad)])


def main():
    print(obtener_decc(10))
    print(obtener_decc(15))
    print(obtener_tupla(10))
    print("Cadena: ",obtener_str(15))


main()