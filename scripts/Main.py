import numpy as np
import random
from tablero import Tablero
from maquina import Maquina
from jugador import Jugador

dimensiones = 10
barcos = [(1, 4), (2, 3), (3, 2), (4, 1)]
tablero_jugador = Jugador(dimensiones, barcos)
tablero_maquina = Maquina(dimensiones, barcos)

#Creating the boards
tablero_jugador.montar_tablero()
tablero_maquina.montar_tablero()


#The game starts
print('''   ¡Bienvenido/a a Hundir la flota!
En este juego deberas hundir todos los barcos de la maquina antes de que ella hunda los tuyos.
Elige fila y columna a la que disparar, si aciertas, se marcará con una X y podrás volver a disparar.
Si fallas, se marcará con una ~ y será el turno de la maquina.
¡Buena suerte!''')

#With the player starting, the game continues until one of the players wins
while True:

#The board to shoot at is shown and the turn is made until it fails
    print('¡Es tu turno!')
    tablero_maquina.mostrar_tablero()
    tablero_jugador.turno(tablero_maquina)

#We check if the player has won. If not, the game continues
    if tablero_jugador.comprobar_ganador(tablero_maquina) == False:
        break

#When the player fails, it is the turn of the machine. It continues until it fails
    print('¡Turno de la maquina!')
    tablero_maquina.turno_maquina(tablero_jugador)

#We check if the machine has won. If not, the game continues
    if tablero_maquina.comprobar_ganador_maquina(tablero_jugador) == False:
        break