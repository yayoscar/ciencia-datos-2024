# Programa que calcula el área de un RECTANGULO
try:
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))

    if base == altura:
        exit("El programa solo calcula rectángulos, no cuadrados")

    area = base * altura

    print(f"El área del rectangulo es {area}")
except ValueError:
    print("Ocurrio un error en la captura, intenta de nuevo")