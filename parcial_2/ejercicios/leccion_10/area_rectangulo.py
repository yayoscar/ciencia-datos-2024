while True:
    try:
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        area = base * altura
        if base == altura:
            exit("Eso es un cuadrado")
        if area.is_integer():
            print("El área es de", int(area))
        else:
            print("El área es de", round(area, 3))
        break
    except ValueError:
        print("Ocurrió un error, intenta de nuevo")
        continue

