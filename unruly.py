"""Lógica del juego Unruly"""

from typing import List, Tuple, Any

Grilla = Any


def crear_grilla(desc: List[str]) -> Grilla:
    """Crea una grilla a partir de la descripción del estado inicial.
    La descripción es una lista de cadenas, cada cadena representa una
    fila y cada caracter una celda. Se puede asumir que la cantidad de las
    filas y columnas son múltiplo de dos. **No** se puede asumir que la
    cantidad de filas y columnas son las mismas.
    Los caracteres pueden ser los siguientes:
    Caracter  Contenido de la celda
    --------  ---------------------
    ' '  Vacío
    '1'  Casillero ocupado por un 1
    '0'  Casillero ocupado por un 0
    Ejemplo:
    >>> crear_grilla([
        '  1 1 ',
        '  1   ',
        ' 1  1 ',
        '  1  0',
    ])
    """

    grilla = []
    for fila in desc: 
        lista = []
        for caracter in fila:
            if caracter != " ":
                lista.append(caracter)
            lista.append(" ")
        grilla.append(lista)
    return grilla

def dimensiones(grilla: Grilla) -> Tuple[int, int]:
    """Devuelve la cantidad de columnas y la cantidad de filas de la grilla
    respectivamente (ancho, alto)"""

    ancho = len(grilla[0])
    "numero de columnas"
    alto = len(grilla)
    "numero de filas"
    return ancho, alto
               
def posicion_es_vacia(grilla: Grilla, col: int, fil: int) -> bool:
    """Devuelve un booleano indicando si la posición de la grilla dada por las
    coordenadas `col` y `fil` está vacía"""
    return grilla[fil][col] == ' '
         
def posicion_hay_uno(grilla: Grilla, col: int, fil: int) -> bool:
        """Devuelve un booleano indicando si la posición de la grilla dada por las
        coordenadas `col` y `fil` está el valor 1"""
        return grilla[fil][col] == '1'

def posicion_hay_cero(grilla: Grilla, col: int, fil: int) -> bool:
    """Devuelve un booleano indicando si la posición de la grilla dada por las
    coordenadas `col` y `fil` está el valor 0"""
    return grilla[fil][col] == '0'

def cambiar_a_uno(grilla: Grilla, col: int, fil: int):
    """Modifica la grilla, colocando el valor 1 en la posición de la grilla
    dada por las coordenadas `col` y `fil`"""
    while True:
        col_a_cambiar, fil_a_cambiar = input("Columna que quiere Cambiar?"), input("Fila que quiere cambiar")
        if not col_a_cambiar.isdigit() and not fil_a_cambiar.isdigit():
            continue
        elif not int(col_a_cambiar) >= 0 and not int(col_a_cambiar) <= col -1 and not int(fil_a_cambiar) >= 0 and not int(fil_a_cambiar) <= col -1:
            continue
        break
    if not grilla[int(fil_a_cambiar)][int(col_a_cambiar)] == '1':
        grilla[int(fil_a_cambiar)][int(col_a_cambiar)] = '1'

def cambiar_a_cero(grilla: Grilla, col: int, fil: int):
    """Modifica la grilla, colocando el valor 0 en la posición de la grilla
    dada por las coordenadas `col` y `fil`"""
    while True:
        col_a_cambiar, fil_a_cambiar = input("Columna que quiere Cambiar?"), input("Fila que quiere cambiar")
        if not col_a_cambiar.isdigit() and not fil_a_cambiar.isdigit():
            continue
        elif not int(col_a_cambiar) >= 0 and not int(col_a_cambiar) <= col -1 and not int(fil_a_cambiar) >= 0 and not int(fil_a_cambiar) <= col -1:
            continue
        break
    if not grilla[int(fil_a_cambiar)][int(col_a_cambiar)] == '0':
        grilla[int(fil_a_cambiar)][int(col_a_cambiar)] = '0'

def cambiar_a_vacio(grilla: Grilla, col: int, fil: int):
    """Modifica la grilla, eliminando el valor de la posición de la grilla
    dada por las coordenadas `col` y `fil`"""
    while True:
        col_a_cambiar, fil_a_cambiar = input("Columna que quiere Cambiar?"), input("Fila que quiere cambiar")
        if not col_a_cambiar.isdigit() and not fil_a_cambiar.isdigit():
            continue
        elif not int(col_a_cambiar) >= 0 and not int(col_a_cambiar) <= col -1 and not int(fil_a_cambiar) >= 0 and not int(fil_a_cambiar) <= col -1:
            continue
        break
    if not grilla[int(fil_a_cambiar)][int(col_a_cambiar)] == ' ':
        grilla[int(fil_a_cambiar)][int(col_a_cambiar)] = ' '

def fila_es_valida(grilla: Grilla, fil: int) -> bool:
    """Devuelve un booleano indicando si la fila de la grilla denotada por el
    índice `fil` es considerada válida.
    Una fila válida cuando se cumplen todas estas condiciones:
        - La fila no tiene vacíos
        - La fila tiene la misma cantidad de unos y ceros
        - La fila no contiene tres casilleros consecutivos del mismo valor
    """
    for x in grilla[fil]:
        if x == " ":
            return False
    for i in range(0,len(grilla[fil])-2):
        if grilla[fil][i] == grilla[fil][i+1] == grilla[fil][i+2]:
            return False
    contar_1=0
    contar_0 = 0
    for elemento in grilla[fil]:
        if elemento == '1':
            contar_0 += 1
            if elemento == '0':
                contar_0 += 1
    if contar_0 != contar_1:
        return False
    return True

def columna_es_valida(grilla: Grilla, col: int) -> bool:
    """Devuelve un booleano indicando si la columna de la grilla denotada por
    el índice `col` es considerada válida.
    Las condiciones para que una columna sea válida son las mismas que las
    condiciones de las filas."""
    for x in grilla:
        if x[col] == " ":
            return False
    for i in range(len(grilla)):
        if grilla[x][col] == grilla[x+1][col] == crear_grilla[x+2][col]:
            return False
    contar_0 = 0
    contar_1 = 0
    for x in grilla:
        if x[col] == "1":
            contar_1 += 1
        elif x[col] == "0":
            contar_0 += 1
    return True

def grilla_terminada(grilla: Grilla) -> bool:

    for fila in grilla():
        if fila_es_valida():
            for columna in grilla():
                if columna_es_valida():
                    return True
    """Devuelve un booleano indicando si la grilla se encuentra terminada.
    Una grilla se considera terminada si todas sus filas y columnas son
    válidas."""

