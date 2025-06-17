import math

def potencia(base, exponente):
    return base ** exponente

def raiz(numero):
    if numero >= 0:
        return math.sqrt(numero)
    else:
        return "Error: raíz de número negativo"
