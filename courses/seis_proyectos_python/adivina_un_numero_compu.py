import random

def imprimir_saludo():
    print()
    print('#####################')
    print('# Adivina un número #')
    print('#  -versión compu   #')
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


def adivina_el_numero(numero, valor_mayor):
    adivina = 0
    cuenta = 0
    bajo = 0
    alto = valor_mayor

    while adivina != numero:
        cuenta += 1

        # Needs to be an integer
        adivina = bajo + (alto - bajo) // 2

        # # Uncomment to debug
        # print(f'DEBUG N: {numero}')
        # print(f'DEBUG B: {bajo}')
        # print(f'DEBUG A: {alto}')

        if adivina < numero:
            bajo = adivina

        if adivina > numero:
            alto = adivina

        print(f'Numero: {numero}   la compu adivina: {adivina}')

    print(f'Número de intentos: {cuenta}')



############
### MAIN ###
############

imprimir_saludo()
valor_mayor = obtener_valor_mayor()
numero = random.randint(0, valor_mayor)
adivina_el_numero(numero, valor_mayor)