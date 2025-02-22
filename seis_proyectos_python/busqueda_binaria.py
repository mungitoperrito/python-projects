import random
import time

MIN = 0
MAX = 500
NUMERO = 2000

def generar_lista(rango, minimo, maximo):
    lista = [random.randint(minimo, maximo) for x in range(rango)]

    return lista


def busqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


def busqueda_binaria(lista, objetivo, min=0, max=None):
    # lista tiene que estar en orden
    if max is None:
        max = len(lista)


    while True:
        punto_medio = (min + max ) // 2

        # # Uncomment to debug
        # print(f'obj: {objetivo}  pm: {punto_medio}  mn: {min}  mx: {max}')

        if lista[punto_medio] == objetivo:
            return punto_medio
        elif lista[punto_medio] > objetivo:
            max = punto_medio
        else:
            min = punto_medio

        if (max - min <= 0):
            return -1


############
### MAIN ###
############

lista_de_valores = generar_lista(NUMERO, MIN, MAX)
lista_de_valores.sort()
objetivo = random.randint(MIN, MAX)

# # Uncomment to debug
# print(f'Lista: {lista_de_valores}')
# print(f'Objectivo: {objetivo}')
# print(f'Obj count: {lista_de_valores.count(objetivo)}')

# Values may repeat
index_ingenua = busqueda_ingenua(lista_de_valores, objetivo)
print(f'Index: {index_ingenua}')

index_binaria = busqueda_binaria(lista_de_valores, objetivo)
print(f'Index: {index_binaria}')
