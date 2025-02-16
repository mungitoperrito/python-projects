import random

def obtener_valor_mayor():
    try:
        valor_mayor = int(input('Entra un numero positivo: '))
    except:
        # Retry if not convirtable to int type
        print('Entra un numero entero positivo como: 13')
        valor_mayor = obtener_valor_mayor()

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
        valor_mayor = obtener_valor(valor_mayor)

    # Check if value is in range
    if (valor > valor_mayor) or (valor < 1):
        valor = obtener_valor(valor_mayor)

    return valor_mayor

def adivina_el_numero(valor_mayor):
    adivinacion = 0
    valor = random.randint(0, valor_mayor)
    print(f'DEBUG: {valor}')
    cuenta = 0

    while adivinacion != valor:
        cuenta += 1
        adivinacion = obtener_valor(valor_mayor)

        if adivinacion < valor:
            print('Demasiado bajo')

        if adivinacion > valor:
            print('Demasiado alto')


    print('Ganaste!')
    print(f'Número de adivinancas: {cuenta}')



############
### MAIN ###
############

print('Adivina un número.')
valor_mayor = obtener_valor_mayor()
adivina_el_numero(valor_mayor)