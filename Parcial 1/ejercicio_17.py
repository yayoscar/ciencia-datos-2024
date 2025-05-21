import random
def lanzar_moneda():
    resultado = random.randint(1, 2)
    if resultado == 1:
        return "Cara"
    else:
        return "Cruz"

while True:
    print("Lanzando moneda...")
    resultado = lanzar_moneda()
    print("El resultado es:", resultado)

    respuesta = input("¿Quieres tirar de nuevo?s/n: ")
    if respuesta.lower() != "s":
        break