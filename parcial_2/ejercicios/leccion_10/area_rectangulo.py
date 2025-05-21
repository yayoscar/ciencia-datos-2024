try:
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))

    if base == altura:
        exit("El programa no calcula cuadrados")
    
    area = base * altura
    print(f"El área del rectángulo es: {area}")
except ValueError:
    print("Hubo un error en la captura, inténtalo de nuevo")