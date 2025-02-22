# Juego del ahorcado

import random
import sys

# Uncomment as needed to test or run
# LISTA_DE_PALABRAS = "lista_de_palabras.txt"
LISTA_DE_PALABRAS = "lista_de_palabras_test.txt"

def imprimir_saludo():
    print()
    print('######################')
    print('# Adivina la palabra #')
    print('######################')
    print()
    print('Para salir, entra -1')
    print()


def escoger_palabra():
    lista_de_palabras = []

    try:
        with open(LISTA_DE_PALABRAS) as f:
            for line in f.readlines():
                lista_de_palabras.append(line.strip())
    except FileNotFoundError:
        print(f"No encuentra el archivo, {LISTA_DE_PALABRAS}.")
    except IOError:
        print(f"Error leyendo el archivo, {LISTA_DE_PALABRAS}.")

    length = len(lista_de_palabras)
    index = random.randint(0, length)
    palabra = lista_de_palabras[index]

    return palabra

def jugar():
    rondas = 0


def obtener_letra():
    letra = input(f'Entra una letra: ')

    if letra == '-1':
        # Exit if -1
        exit()
    elif len(letra) > 1:
        print("Solo una letra.")
        obtener_letra()

    # No error handling for non-letters

    return letra
