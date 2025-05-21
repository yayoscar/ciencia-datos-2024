import math

def perimetro_rectangulo(ancho, alto):
    return 2 * (ancho + alto)

def perimetro_cuadrado(lado):
    return 4 * lado

def perimetro_hexagono(lado):
    return 6 * lado

def perimetro_pentagono(lado):
    return 5 * lado

def perimetro_rombo(lado):
    return 4 * lado

def perimetro_trapecio(base1,  base2, altura):
  lado1 = math.sqtr((base1/2) **altura** 2)
  lado2 = math.sqrt((base1 / 2) ** 2 + altura ** 2)
  return base1 + base2 + lado1 +lado2
def perimetro_circulo(radio):
    return 2 + math.pi * radio
def main():
    print("menu de calculos de perimetro")
    print("______________________________")
    print("1 perimetro_rectangulo")
    print("2 cuadrado")
    print("3 hexagono")
    print("4 pentagono")
    print("5 Rombo")
    print("6 Trapecio")
    print("7 Circulo")
    print("8, salir")
    opcion = input("seleccione una opcion:")

    if opcion == "1":
        ancho = float(input("ingresa el ancho del rectangulo"))
        alto = float(input("ingresa el alto del rectangulo"))
        print ("El perimetro del rectangulo es:" ,perimetro_rectangulo(ancho, alto),)
    elif opcion == "2":
        lado = float(input("ingrese el alto del cuadrado"))
        print("el perimetro del cuadrado"), perimetro_cuadrado(lado)
    elif opcion == "3":
        lado = float(input("ingresa el lado del hexagono"))
        print("el perimetro del hexagono es",perimetro_hexagono(lado))
    elif opcion == "4":
        lado = float(input("ingrese el lado del pentagono:  "))
        print("el perimetro del pentagono es:",perimetro_pentagono(lado))
    elif opcion == "5":
        lado = float(input("ingresa el lado del rombo: "))
        print("el perimetro del rombo es:", perimetro_rombo(lado))
    elif opcion == "6":
        base1 = float(input("ingresa la base 1 del trapecion"))
        base2 = float(input("ingresa la base 2 del trapecio"))
        altura = float(input("ingresa la altura del trapecio"))
        print("el perimetro del trapecio es:", perimetro_trapecio(base1,base2,altura))
    elif opcion == "7":
        radio = float(input("ingresa el radio del circulo"))
        print("el perimetro del circulo es:", perimetro_circulo(radio))
    elif opcion == "8":
        print("gracias por utilizae este programa.")
        breakpoint()
    else:
        print("opcion invalida.porfavor seleccione otra opcion")
if __name__=="__main__":
    main()










