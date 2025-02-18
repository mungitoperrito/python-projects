import random
import sys

def escoger():
    eleccion = ''

    r = random.randint(0,2)
    if r == 0:
        eleccion = 'piedra'
    elif r == 1:
        eleccion = 'papel'
    else:
        eleccion = 'tijeras'

    return eleccion

def jugar():
    rondas = 0
    jugadores = ['jugador_01', 'jugador_02']

    while True:
        jugador_01 = escoger()
        jugador_02 = escoger()
        print(f'Jugador 01: {jugador_01}  Jugador 02: {jugador_02}')
        esta_ronda = [jugador_01, jugador_02]

        rondas += 1

        if jugador_01 == jugador_02:
            continue
        elif ('papel' in esta_ronda) and ('piedra' in esta_ronda):
            idx = esta_ronda.index('papel')
        elif ('papel' in esta_ronda) and ('tijeras' in esta_ronda):
            idx = esta_ronda.index('tijeras')
        elif ('tijeras' in esta_ronda) and ('piedra' in esta_ronda):
            idx = esta_ronda.index('piedra')
        else:
            print('Error')

        print(f'Gana: {jugadores[idx]} en {rondas} ronda(s).')
        sys.exit()


############
### MAIN ###
############

jugar()