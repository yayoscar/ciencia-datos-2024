import random
def lanzar_moneda():
    resultado = random.randint(1, 2)
    if resultado == 1:
        return "Aguila"
    else:
        return "Sol"

while True:
    print("Lanzando la moneda...")
    resultado = lanzar_moneda()
    print("El resultado es:", resultado)

    respuesta = input("¿Quiéres tirar de nuevo?S/N: ")
    if respuesta.lower() != "s":
        break