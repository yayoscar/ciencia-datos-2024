def rectangulo (b,h):
    perimetro=(2*b)+(2*h)
    return perimetro

def cuadrado (lados):
    perimetro=(4*lados)
    return perimetro

def hexagono (lados):
    perimetro=(6*lados)
    return perimetro


def pentagono (lados):
    perimetro=(5*lados)
    return perimetro

def rombo (lados):
    perimetro=(4*lados)
    return perimetro

def trapecio (B,b,l):
    perimetro=(B+b+(2*l))
    return perimetro

def circulo (diametro):
    perimetro=(diametro*3.14)
    return perimetro

continuar=True
while continuar:
    print("1.perimetro de rectangulo")
    print("2.perimetro de cudrado")
    print("3.perimetro de exagono")
    print("4.perimetro de pentagono")
    print("5.perimetro de rombo")
    print("6.perimetro de trapecio")
    print("7.perimetro de circulo")
    print("8.salir")
    escribir_mensaje = str(input("¿selecciona una opcion"))

    if escribir_mensaje == "8":
        mensaje = input("hasta luego bro")
        continuar = False
    elif escribir_mensaje=="1":
        b = float(input(print("ingrese e valor de la base")))
        h = float(input(print("ingrese e valor de la altura")))
        print("el resultado es")
        print(rectangulo (b,h))

    elif escribir_mensaje == "2":
        lados  = float(input(print("ingrese e valor de los lados ")))
        print("el resultado es")
        print(cuadrado (lados))

    elif escribir_mensaje == "3":
       lados = float(input(print("ingrese e valor de los lados ")))
       print("el resultado es")
       print(hexagono(lados))

    elif escribir_mensaje == "4":
         lados  = float(input(print("ingrese e valor de los lados ")))
         print("el resultado es")
         print(pentagono (lados))


    elif escribir_mensaje == "5":
        lados = float(input(print("ingrese e valor de los lados ")))
        print("el resultado es")
        print(rombo(lados))

    elif escribir_mensaje == "6":
        B = float(input(print("ingrese e valor de la base mayor")))
        b= float(input(print("ingrese e valor de la base menor")))
        l =float(input(print("ingrese el lado")))
        print("el resultado es")
        print(trapecio (B,b,l))

    elif escribir_mensaje == "7":
        diametro  = float(input(print("ingrese el valor del diametro")))
        print("el resultado es")
        print(circulo (diametro*3.14))

