import random
import timeit

NUMERO = 100000

# Comment to test
MIN = -1 * NUMERO
MAX = NUMERO

# # Uncomment to test
# MIN = -10
# MAX = 10

def generar_lista(rango, minimo, maximo):
    lista = [random.randint(minimo, maximo) for x in range(rango)]

    return lista


def busqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


def busqueda_binaria(lista, objetivo):
    # lista tiene que estar en orden
    min = 0
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

        if (max - min <= 1):
            return -1


############
### MAIN ###
############

if __name__ == '__main__':
    lista_de_valores = generar_lista(NUMERO, MIN, MAX)
    lista_de_valores.sort()
    objetivo = random.randint(MIN, MAX)

    # # Uncomment to test not found
    # objetivo = MAX + 1

    # # Uncomment to debug
    # print(f'Lista: {lista_de_valores}')
    # print(f'Objectivo: {objetivo}')
    # print(f'Obj count: {lista_de_valores.count(objetivo)}')
    # try:
    #     print(f'idx: {lista_de_valores.index(objetivo)}')
    # except:
    #     print(f'{objetivo} is not in list')

    # Values may repeat, so the index may differ if there is a
    #   series of objetivo values in lista_de_valores

    # # Uncomment to run untimed
    # index_ingenua = busqueda_ingenua(lista_de_valores, objetivo)
    # print(f'Index: {index_ingenua}')

    # index_binaria = busqueda_binaria(lista_de_valores, objetivo)
    # print(f'Index: {index_binaria}')

    # Uncomment to time runs
    inicio =  timeit.time.perf_counter_ns()
    index_ingenua = busqueda_ingenua(lista_de_valores, objetivo)
    print(f'Index: {index_ingenua}',
          f'\tingenio: {timeit.time.perf_counter_ns() - inicio}'
         )

    inicio =  timeit.time.perf_counter_ns()
    index_binaria = busqueda_binaria(lista_de_valores, objetivo)
    print(f'Index: {index_binaria}',
          f'\tbinario: {timeit.time.perf_counter_ns() - inicio}'
         )
