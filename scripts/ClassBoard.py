import numpy as np
import random

#Creating the board class
class Tablero:
    def __init__(self, dimensiones, barcos):
        self.dimensiones = dimensiones
        self.barcos = barcos
        self.tablero = np.full((self.dimensiones, self.dimensiones), ' ')

    #Creating the method to place all the ships on the board
    def montar_tablero(self):
        for barco in self.barcos:
            while True:
                fila = random.randint(0, self.dimensiones - 1)
                columna = random.randint(0, self.dimensiones - 1)
                orientacion = random.randint(0, 1)
                if self.validar_posicion(fila, columna, barco, orientacion):
                    if orientacion == 0:
                        for i in range(barco[1]):
                            self.tablero[fila, columna + i] = 'O'
                    else:
                        for i in range(barco[1]):
                            self.tablero[fila + i, columna] = 'O'
                    break

    #Creating the method to validate the position of the ships
    def validar_posicion(self, fila, columna, barco, orientacion):
        if orientacion == 0:
            if columna + barco[1] > self.dimensiones:
                return False
            for i in range(barco[1]):
                if self.tablero[fila, columna + i] != ' ':
                    return False
        else:
            if fila + barco[1] > self.dimensiones:
                return False
            for i in range(barco[1]):
                if self.tablero[fila + i, columna] != ' ':
                    return False
        return True

 #Creating the method to show the board of the machine with the shots of the player, without showing the ships
    def mostrar_tablero(self):
        ver_tablero = np.where(self.tablero_sin_barcos == 'O', ' ', self.tablero_sin_barcos)
        disparos = np.where(self.tablero == 'X', 'X', ' ')
        fallos= np.where(self.tablero == '~', '~', ' ')
        tablero_con_disparos = np.where(disparos != ' ', disparos, np.where(fallos != ' ', fallos, ver_tablero))
        print(tablero_con_disparos)

