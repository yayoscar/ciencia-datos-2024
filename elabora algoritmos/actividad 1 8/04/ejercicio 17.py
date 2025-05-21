import random

def lanzar_moneda():
    resultado = random.choice(["Cara", "sol"])
    return resultado
print("Lanzamiento de la moneda:")
print("Resultado:", lanzar_moneda())