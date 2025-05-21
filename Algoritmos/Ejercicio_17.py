import random
def lanzar_moneda():
    return random.choice(['cara', 'sol'])
while True:
    resultado = lanzar_moneda()
    print("Al lanzar la moneda el resultado fue: ", resultado)
    repetir=input("¿Desea lanzar la moneda de nuevo? (s/n): ").strip().lower()
    if repetir != "s":
        print("Bye")
        break