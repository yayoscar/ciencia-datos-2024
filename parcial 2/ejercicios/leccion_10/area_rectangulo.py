  #
try:
    base = float(input("ingresa la base del rectangulo"))
    altura = float(input("imgresa la altura del rectangullo"))

    if base== altura:
        exit("el programa solo calcula rectangulos no cuadrados")
    area = base*altura
    print(f"la area del rectangulo es {area})")
except ValueError:
       print("ocurrio un error en la captura intenta de nuevo")