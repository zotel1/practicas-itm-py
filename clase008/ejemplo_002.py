"""
eliminamos un objeto de una lista con un while
"""

lista = [1,2,3,4,5,6,7,1,1,8,1,1,9,10]
print(lista)

x = 0

while(x < len(lista)):
    
    if (lista[x] == 1):
        lista.pop(x)
        print(lista)
    else:
        x += 1
print(lista)