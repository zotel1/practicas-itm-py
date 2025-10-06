


def cuadrado(x):
    x = int(input("Ingrese un numero: "))
    return x * x


#PROGRAMA PRINCIPAL
def main():
    resultado_uno = cuadrado(2)
    resultado_dos = cuadrado(3)
    resultado_tres = cuadrado(4)
    resultado_cuatro = cuadrado(5)

    print(f"resultado_uno {resultado_uno}")
    print(f"resultado_dos {resultado_dos}")
    print(f"resultado_tres {resultado_tres}")
    print(f"resultado_cuatro {resultado_cuatro}")


main() # <== PUNTO DE ENTRADA