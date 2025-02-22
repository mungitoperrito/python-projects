# Juego del ahorcado

import random

from dibujos import dibujos


# Uncomment as needed to test or run
LISTA_DE_PALABRAS = "lista_de_palabras.txt"
# LISTA_DE_PALABRAS = "lista_de_palabras_test.txt"


def imprimir_saludo():
    print()
    print('######################')
    print('# Adivina la palabra #')
    print('######################')
    print()
    print('Para salir, entra -1')
    print()


def escoger_palabra():
    # Compare explicit file open and process with python import method
    #    for importing the drawings

    lista_de_palabras = []

    try:
        with open(LISTA_DE_PALABRAS, encoding="utf-8") as f:
            for line in f.readlines():
                lista_de_palabras.append(line.strip())
    except FileNotFoundError:
        print(f"No encuentra el archivo, {LISTA_DE_PALABRAS}.")

    # No error handling for blank lines, broken lines

    length = len(lista_de_palabras)
    index = random.randint(0, length - 1)
    palabra = lista_de_palabras[index]

    return palabra


def update_palabra(palabra_letras, palabra, letra):
    index = 0

    while True:
        index = palabra.find(letra, index)
        if index == -1:
            break
        else:
            palabra_letras[index] = letra
            index += 1

    return palabra_letras


def jugar(palabra):
    rondas = 0
    palabra = palabra.upper()
    palabra_letras = ['_' for x in list(palabra)]
    letras_adivinadas = set()
    vidas = 6
    # print(palabra) # DEBUG
    # print(palabra_letras) # DEBUG

    print(f'La palabra es: {palabra_letras}')

    while vidas > 0:
        rondas += 1

        letra = obtener_letra()
        if letra in letras_adivinadas:
            print(f"Ya advinaste {letra}")
            continue
        else:
            letras_adivinadas.add(letra)

        if letra in palabra:
            palabra_letras = update_palabra(palabra_letras, palabra, letra)
            if '_' not in palabra_letras:
                print(f'\n¡Ganaste en {rondas} rondas!')
                exit()
        else:
            vidas -= 1

        # Update info for this round
        print(dibujos[vidas])
        print(f'Tienes: {palabra_letras}')
        print(f'Adivinada: {sorted(letras_adivinadas)}')
        print("\n")


def obtener_letra():
    letra = input(f'Entra una letra: ')

    if letra == '-1':
        # Exit if -1
        exit()
    elif len(letra) > 1:
        print("Solo una letra.")
        obtener_letra()

    # No error handling for non-letters

    return letra.upper()


############
### MAIN ###
############

imprimir_saludo()
palabra = escoger_palabra()
jugar(palabra)
