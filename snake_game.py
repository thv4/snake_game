import os
import readchar
import random

ANCHO = 30
ALTURA = 25
POS_X = 0
POS_Y = 1
Numero_fichas = 15

mi_posicion = [2,4]
fichas = []
cola = []
tamaño_cola = 0
final_juego = False


while final_juego != True:
    while len(fichas) < Numero_fichas:
        nuevos_objetos = [random.randint(0, ANCHO), random.randint(0, ALTURA)]
        if nuevos_objetos not in fichas and nuevos_objetos != mi_posicion:
            fichas.append(nuevos_objetos)

    print("-" * ANCHO * 3)

    for al in range(ALTURA):
        print("|", end="")
        for an in range(ANCHO):
            dibujo = " "
            modificar_objeto = None
            modificar_cola = None
            for ficha in fichas:
                if ficha[POS_X] == an and ficha[POS_Y] == al:
                    dibujo = "*"
                    modificar_objeto = ficha
            for colita in cola:
                if colita[POS_X] == an and colita[POS_Y] == al:
                    dibujo = "+"
                    modificar_cola = colita
            if mi_posicion[POS_X] == an and mi_posicion[POS_Y] == al:
                dibujo = "@"
                if modificar_objeto:
                    fichas.remove(modificar_objeto)
                    tamaño_cola += 1
                if modificar_cola:
                    print("Has perdido", end="")
                    final_juego = True
            print(" {} ".format(dibujo), end="")
        print("|")

    print("-" * ANCHO * 3)

    print("W/A/S/D para moverte:")
    mover = readchar.readchar().decode()

    if mover.upper() == "W":
        cola.insert(0,mi_posicion.copy())
        cola = cola[:tamaño_cola]
        mi_posicion[POS_Y] -= 1
        mi_posicion[POS_Y] %= ALTURA
    elif mover.upper() == "S":
        cola.insert(0,mi_posicion.copy())
        cola = cola[:tamaño_cola]
        mi_posicion[POS_Y] += 1
        mi_posicion[POS_Y] %= ALTURA
    elif mover.upper() == "A":
        cola.insert(0,mi_posicion.copy())
        cola = cola[:tamaño_cola]
        mi_posicion[POS_X] -= 1
        mi_posicion[POS_X] %= ANCHO
    elif mover.upper() == "D":
        cola.insert(0,mi_posicion.copy())
        cola = cola[:tamaño_cola]
        mi_posicion[POS_X] += 1
        mi_posicion[POS_X] %= ANCHO
    elif mover.upper() == "E":
        final_juego = True

    os.system("cls")





