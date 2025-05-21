import random

def lanzar_moneda():
    return random.choice(['Cara', 'Cruz'])

while True:
    resultado = lanzar_moneda()
    print("Resultado del lanzamiento: ",resultado)

    repetir=input("¿Quieres lanzar la moneda otra vez? (s/n):").strip().lower()
    if repetir != 's':
        print("¡Hasta luego!")
        break