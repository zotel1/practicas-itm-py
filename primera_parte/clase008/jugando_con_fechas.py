import sys
sys.path.append('recursos/')
import fechas_int as fech

for cadena in sys.path:
    print(cadena)




def main():
    print(fech.str_fecha(20211221))
    fech.el_dia()


main()
