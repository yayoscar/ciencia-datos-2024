try:
    base = float(input("ingrese la base "))
    altura = float(input("ingrese la altura "))
    if base== altura:
        exit("El programa solo calcula area de rectangulo")

    area = base + altura
    print(f"el area del rectangulo es",area)
except ValueError:
    print("ingrese de nuevo")







