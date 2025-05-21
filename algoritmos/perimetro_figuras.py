def rectangulo(b, h):
    perimetro = (2 + b) * (2 + h)
    return perimetro


def cuadrado(lado):
    perimetro = 4 * lado
    return perimetro


def hexagono(lado):
    perimetro = 6 * lado
    return perimetro


def pentagono(lado):
    perimetro = 5 * lado
    return perimetro


def rombo(lado):
    perimetro = 4 * lado
    return perimetro


def trapecio(B, b, lado):
    perimetro = (B + b) + (2 * lado)
    return perimetro


def circulo(diametro):
    perimetro = 3.14 * diametro
    return perimetro


continuar = True
while continuar:
    print("Programa que calcula el perímetro de las siguientes figuras: ")
    print("Rectángulo")
    print("Cuadrado")
    print("Hexágono")
    print("Pentágono")
    print("Rombo")
    print("Trapecio")
    print("Círculo")
    figura = input("¿Qué figura desea realizar? ").capitalize()

    if figura == "Rectángulo":
        b = int(input("Ingrese la base: "))
        h = int(input("Ingrese la altura: "))
        print(rectangulo(b, h))
    elif figura == "Cuadrado":
        lado = int(input("Ingrese el lado del cuadrado: "))
        print(cuadrado(lado))
    elif figura == "Hexágono":
        lado = int(input("Ingrese el lado del hexágono: "))
        print(hexagono(lado))
    elif figura == "Pentágono":
        lado = int(input("Ingrese el lado del pentágono: "))
        print(pentagono(lado))
    elif figura == "Rombo":
        lado = int(input("Ingrese el lado del rombo: "))
        print(rombo(lado))
    elif figura == "Trapecio":
        B = int(input("Ingrese la base mayor: "))
        b = int(input("Ingrese la base menor: "))
        lado = int(input("Ingrese el lado: "))
        print(trapecio(B, b, lado))
    elif figura == "Círculo":
        diametro = int(input("Ingrese el diámetro del círculo: "))
        print(circulo(diametro))
    else:
        print("No entendí.")

    continuar = input("¿Desea calcular otra figura? (sí/no): ").lower() == "sí"



