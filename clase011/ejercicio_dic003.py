




def obtener_dic(lista_productos):
    d = {str:list[str]}
    for _,nombre,_,categoria in lista_productos:
        if categoria in d.keys():
            d[categoria].append(nombre)
        else:
            d[categoria] = [nombre]










def main():
    pass




main()