"""
aaaamm | ==> dd
"""

def el_dia(aaaammdd):
    return (aaaammdd %100)

"""
aaaa | ==> mm <==| dd
"""
def el_mes(aaaammdd):
    return (aaaammdd // 10000)%100

"""
aaaa <== | mmdd"""
def el_anio(aaaammdd):
    return (aaaammdd // 10000)

def str_fecha(aaaammdd):
    return f"{el_dia(aaaammdd):02}/{el_mes(aaaammdd):02}/{el_anio(aaaammdd):04}"

def es_biciesto(anio):
    return anio%4 == 0

def obtener_cantidad_dias_mes(mes, anio):
    dias = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    # index 0, 1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12
    if mes == 2 and es_biciesto(anio):
        return 29
    return dias[mes]
def es_fecha_valida(aaaammdd):
    anio = el_anio(aaaammdd)
    if (anio < 1):
        return False
    mes = el_mes(aaaammdd)
    if(mes < 1 or mes > 12):
        return False
    dia = el_dia
    if(dia < 1 or dia > obtener_cantidad_dias_mes(mes, anio)):
        return False
    return True
    

def main():

    fecha = 199692 ##AAAMMDD
    print(str_fecha(fecha))

#    dia = el_dia(fecha)
 #   mes = el_mes(fecha)
  #  anio = el_anio(fecha)


# TAREA MOSTRAR TODAS LAS FECHAS DEL AÑO 2001 utilizando un for








main()