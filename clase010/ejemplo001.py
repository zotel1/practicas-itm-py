import sys
sys.path.insert(0,'recursos/')
import funciones as fun
import datos
import random

def crear_lista_personas(cantidad:int)->list:
    lista = []
    
    for x in range(cantidad):
        lista.append([datos.obtener_nombre_completo(),random.randint(18, 75)])
    return lista

def orden_edad(lista)->int:
    return lista[1]

def orden_nombre_completo(lista)->int:
    return lista[0]

def orden_apellido(lista)->int:
    #return lista[0].split(',')[0]
    apellido, nombre = lista[0].split(',')
    cadena = apellido.lower().replace(' ', '')+nombre.lower().replace(' ', '')
    print(cadena)
    return cadena

def main():
    personas = crear_lista_personas(30)
    personas.sort(key=orden_apellido)
    for p in personas:
        print(p)


main()