import random

def imprimir_saludo():
    print()
    print('#####################')
    print('# Adivina un número #')
    print('#####################')
    print()
    print('Para salir, entra -1')
    print()

def salir(valor):
    if valor == -1:
        exit()


def obtener_valor_mayor():
    try:
        valor_mayor = int(input('Entra un numero positivo: '))
    except:
        # Retry if not convirtable to int type
        print('Entra un numero entero positivo como: 13')
        valor_mayor = obtener_valor_mayor()

    # Exit if -1
    salir(valor_mayor)

    # Check if  0 or negative
    if (valor_mayor < 1):
        valor_mayor = obtener_valor_mayor()

    return valor_mayor


def obtener_valor(valor_mayor):
    try:
        valor = input(f'Entra un numero entre 1 y {valor_mayor} (inclusivo): ')
        valor = int(valor)
    except:
        # Retry if not convirtable to int type
        print('Entra un numero entero positivo como: 5')
        valor = obtener_valor(valor_mayor)

    # Exit if -1
    salir(valor)

    # Check if value is in range
    if (valor > valor_mayor) or (valor < 1):
        valor = obtener_valor(valor_mayor)

    return valor


def adivina_el_numero(valor_mayor):
    adivina = 0
    valor = random.randint(0, valor_mayor)
    # print(f'DEBUG: {valor}')
    cuenta = 0

    while adivina != valor:
        cuenta += 1
        adivina = obtener_valor(valor_mayor)

        if adivina < valor:
            print('Demasiado bajo')

        if adivina > valor:
            print('Demasiado alto')


    print('Ganaste!')
    print(f'Número de intentos: {cuenta}')



############
### MAIN ###
############

imprimir_saludo()
valor_mayor = obtener_valor_mayor()
adivina_el_numero(valor_mayor)