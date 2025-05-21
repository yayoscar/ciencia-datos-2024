#simular el lanzamiento de una moneda importando random y usando .randint(1,2), preguntar al usuario si quiere tirar de nuevo
import random

def lanzar_moneda():
    resultado = random.randint(1, 2)
    if resultado == 1:
        return "Cara"
    else:
        return "Cruz"

while True:
    print("Resultado:", lanzar_moneda())
    repetir = input("¿Quieres lanzar de nuevo? (s/n): ").strip().lower()
    if repetir != 's':
        print("¡Hasta la próxima!")
        break
