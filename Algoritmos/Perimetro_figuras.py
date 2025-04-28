def rectangulo(b,h):
    perimetro= (2*b)+(2*h)
    return perimetro

def cuadrado(lado):
    perimetro= (4*lado)

def hexagono(lado):
    perimetro= (6*lado)

def pentagono(lado):
    perimtero= (5*lado)

def rombo(lado):
    perimetro= (4*lado)

def trapecio(B,b,l):
    perimetro= (B)+(b)+(2*l)

    pi = 3.1416
def circulo(pi,D):
    perimetro=(pi*D)

print("rectangulo")
print("cuadrado")
print("hexagono")
print("pentagono")
print("rombo")
print("trapecio")
print("circulo")

figura = input("ingrese el nombre de la figura que desea saber su perimetro: ")

if figura == "rectangulo":
   b = int(input("ingrese 2*b"))
   h = int(input("ingrese 2*h"))
   print(rectangulo(b, h))
elif figura == "cuadrado":
        lado = int(input("ingrese 4*lado"))
        print(cuadrado(4*lado))
elif figura == "hexagono":
        lado = int(input("ingrese 6*lado"))
        print(hexagono(6*lado))
if figura == "pentagono":
    lado = int(input("ingrese 5*lado"))
    print(pentagono(5*lado))

if figura == "rombo":
    lado = int(input("ingrese 4*lado"))
    print(rombo(4*lado))

if figura == "trapecio":
    B,b,l = int(input("ingrese B,b,2*l"))

if figura == "circulo":
    lado = int(input("ingrese pi*D"))
    print(circulo(3.1416*D))
