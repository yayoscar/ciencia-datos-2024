import math
def potencia(base, exponente):
    return base ** exponente

def raíz(numero):
    if numero >= 0:
      return math.sqrt(numero)
    else:
        return "Error: raíz de numero negativo"
