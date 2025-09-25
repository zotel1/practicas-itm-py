"""
Una cadena de comida rápida solicita el desarrollo de una aplicación para sus 
terminales de autoservicio que permita a los clientes armar su propio menú.
Los clientes pueden elegir diferentes opciones de combos o pedir por 
separado la comida, bebida y postre.

Al iniciar la aplicación, se debe mostrar el siguiente menú de opciones:
1) Combo 1: Hamburguesa, papas fritas y gaseosa - $1550
2) Combo 2: Hamburguesa con queso, papas fritas y gaseosa - $1650
3) Hamburguesa sola - $1300
4) Hamburguesa con queso - $1400
5) Gaseosa - $700
6) Postre - $600
7) Agregar aderezo - $100
() Terminar

Luegro de seleccionar cada ítem, se debe mostrar el subtotal para que el cliente
pueda decidir si desea agregar más productos a su pedido antes de terminar.
"""
import sys
sys.path.insert(0, 'recursos/')

TUPLA_OPCIONES = (
"1) Combo 1: Hamburguesa, papas fritas y gaseosa - $1550",
"2) Combo 2: Hamburguesa con queso, papas fritas y gaseosa - $1650",
"3) Hamburguesa sola - $1300",
"4) Hamburguesa con queso - $1400",
"5) Gaseosa - $700",
"6) Postre - $600",
"7) Agregar aderezo - $100",
"8) Terminar")

def menu(tupla_opciones):
    
    for opcion in tupla_opciones:
        print(opcion)

def main():
    terminar_programa = False
    while( not terminar_programa):
        opcion = menu(TUPLA_OPCIONES)



if __name__== '__main__':
    main()