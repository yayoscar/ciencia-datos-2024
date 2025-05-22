try:
    base = float(input("ingrese la base: "))
    altura = float(input("ingrese la altura: "))
    if base == altura:
        exit("el programa solo calcula rectangulos, no cuadrados")
    area = base * altura
    print(f"El area del rectangulo es {area}")
except ValueError:
    print("ocurrio un error en la captura, intente denuevo")
