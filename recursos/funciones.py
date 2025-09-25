"""

Este Módulo implementa funciones de uso general.

- es_entero(str_numero)
- es_flotante(str_numero)
- es_entero_entre(str_numero)
- es_flotante_entre(str_numero)

"""
def leer_entero():
    pass

def menu(tupla_opciones:tuple[str])->int:
    tupla_opciones
    for index,opcion in enumerate(tupla_opciones,1):
        print(f"{index} {opcion}")
    return leer_entero("Ingrese una opcion: ", 1)