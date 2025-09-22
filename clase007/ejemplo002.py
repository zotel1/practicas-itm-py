

def es_entero(cadena):

    # BLOQUES VIGILADOS
    try:
        int(cadena)
        
    except: # SI EXISTE UN ERROR
        return False
    return True # SI NO EXISTE UN ERROR

def es_numero(cadena):
    return es_entero(cadena) or es_float(cadena)
    

def es_float(cadena):

    # BLOQUES VIGILADOS
    try:
        float(cadena)
        return True
    except:
        return False



def leer_un_entero(cartel):
    datos_ok = False

    while( not datos_ok): # datos_ok == False):
        cadena = input(cartel)
        if(es_entero(cadena)):
            numero = int(cadena)
            datos_ok = True
        else:
            print(f"Error: '{cadena}' No es un numero.")
    return numero

def leer_un_float(cartel):
    datos_ok = False

    while( not datos_ok): # datos_ok == False):
        cadena = input(cartel)
        if(es_float(cadena)):
            numero = float(cadena)
            datos_ok = True
        else:
            print(f"Error: '{cadena}' No es un float.")
    return numero

def main():
    dia = leer_un_entero("Dia:")
    mes = leer_un_entero("Mes:")
    print(dia)
    print(mes)

    


main()