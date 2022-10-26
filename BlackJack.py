import random
from pedir_numero import pedir_entrada_numero_delimitado

cartas = {
    chr(0x1f0a1): 1,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 11,
    chr(0x1f0ad): 12,
    chr(0x1f0ae): 13,
}
baraja = (list(cartas.values())) * 4

def simbolo_carta(carta):
    if carta == 1:
        carta = chr(0x1f0a1)
    elif carta == 2:
        carta = chr(0x1f0a2)
    elif carta == 3:
        carta = chr(0x1f0a3)
    elif carta == 4:
        carta = chr(0x1f0a4)
    elif carta == 5:
        carta = chr(0x1f0a5)
    elif carta == 6:
        carta = chr(0x1f0a6)
    elif carta == 7:
        carta = chr(0x1f0a7)
    elif carta == 8:
        carta = chr(0x1f0a8)
    elif carta == 9:
        carta = chr(0x1f0a9)
    elif carta == 10:
        carta = chr(0x1f0aa)
    elif carta == 11:
        carta = chr(0x1f0ab)
    elif carta == 12:
        carta = chr(0x1f0ad)
    else:
        carta = chr(0x1f0ae)
    return carta

def puntuacion(carta, total):
    if carta == 1:
        total += 11
    elif carta == 2:
        total += 2
    elif carta == 3:
        total += 3
    elif carta == 4:
        total += 4
    elif carta == 5:
        total += 5
    elif carta == 6:
        total += 6
    elif carta == 7:
        total += 7
    elif carta == 8:
        total += 8
    elif carta == 9:
        total += 9
    elif carta == 10:
        total += 10
    elif carta == 11:
        total += 10
    elif carta == 12:
        total += 10
    elif carta == 13:
        total += 10
    return total

def carta_inicial(baraja):
    mano = []
    total = 0
    for i in range(2):
        random.shuffle(baraja)
        carta = baraja.pop()
        puntos = puntuacion(carta, 0)
        total += puntos
        carta = simbolo_carta(carta)
        mano.append(carta)
    return mano, total

def pedir_carta(mano, total, baraja):
    carta = baraja.pop()
    if carta == 1:
        puntos = 11
    elif carta == 11:
        puntos = 10
    elif carta == 12:
        puntos = 10
    elif carta == 13:
        puntos = 10
    else:
        puntos = carta
    total += puntos
    carta = simbolo_carta(carta)
    mano.append(carta)
    return mano, total