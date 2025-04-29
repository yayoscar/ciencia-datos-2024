try:
    base= float(input(("ingrese la base: ")))
    altura= float(input(("ingrese la altura: ")))
    if altura == base:
        exit("el programa solo calcula rectá    ngulos, no cuadrados")

    area = base * altura

    print((f"El area del rectangulo es {area}"))
except ValueError:
    print("ocurrio un erro en la captura ,intente de nuevo")

