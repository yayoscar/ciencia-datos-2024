def area(base,altura):
    return base * altura

base =float(input("ingrese la base: "))
altura = float(input("ingrese la altura: "))

if base == altura:
    print("el programa solo cata rectangulos, no cuadrados")
else:

        print(f"el area del rectangulo es:", area(base,altura))
