

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

def leer_un_entero_entre_dias(cartel, desde, hasta):
    while(True):
        cadena = input(cartel)
        if(es_entero(cadena)):
            numero = int(cadena)
            if desde <= numero <= hasta:
                return numero
            else:
                print(f"Error: '{numero}' esta fuera de rango[{desde, hasta}]")
        else:
            print(f"Error: '{cadena}' No es un numero.")
    
def leer_un_entero_entre_meses(cartel, desde, hasta):
    while(True):
        cadena = input(cartel)
        if(es_entero(cadena)):
            numero = int(cadena)
            if desde <= numero <= hasta:
                return numero
            else:
                print(f"Error: '{numero}' esta fuera de rango[{desde, hasta}]")
        else:
            print(f"Error: '{cadena}' No es un numero.")
    

def main():
    dia = leer_un_entero_entre_dias("Dia: ", 1,31)
    mes = leer_un_entero_entre_meses("Mes: ",1,12)
    
    print(f"Elegiste el dia {dia}, del mes {mes}")

    


main()