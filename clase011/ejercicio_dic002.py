"""
Invierte las llaves y los valores del diccionario que contiene los cuadrados,
de tal manera que los cuadrados sean las llaves y los números originales
sean los valores.
"""

def obtener_dicc(n:int)->dict:
    return {x:x**2 for x in range(n)}

def main():

    dic = obtener_dicc(10)
    otro = { v:k for k,v in dic.items()}
    print("Primer diccionario",dic)
    print("Segundo diccionario, invertido, ahora tenemos valor y clave: ",otro)


main()