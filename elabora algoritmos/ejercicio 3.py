def rectangulo (b,h):
    perimetro=(2*b)+(2*h)
    return perimetro
def cuadrado(lado):
    perimetro=(4*lado)
    return perimetro
def hexagono(lado):
    perimetro=(6*lado)
    return perimetro
def pentagono(lado):
    perimetro=(5*lado)
    return perimetro
def rombo(lado):
    perimetro = (4 * lado)
    return perimetro
def trapecio(b,l):
    perimetro = (b+b)+(2*l)
    return perimetro
def circulo(pi,d):
    pi=3.14
    perimetro = (pi*d)
    return perimetro
print('1.rectangulo')
print('2.cuadrado')
print('3.hexagono')
print('4.pentagono')
print('5.rombo')
print('6.trapecio')
print('7.circulo')
calcular=input('Que perimetro deseas calcular')
match calcular:
    case "1":
        b=float(input('ingrese la base del rectangulo'))
        h=float(input('ingrese la altura del rectangulo'))
        print('el perimetro del rectangulo es:')
        print(rectangulo(b,h))

    case '2':
        l=float(input('ingrede el valor de uno de los lados de cuadrado'))
        print('el perimetro del cuadrado es:')
        print(cuadrado(l))
    case '3':
        l=float(input('ingre el valor de uno de los lados del hexagono'))
        print('el perimetro del hexagono es:')
        print(hexagono(l))
    case '4':
        l=float(input('ingre el valor de uno de los lados del pentagono'))
        print('el perimetro del pentagono es:')
        print(pentagono(l))
    case '5':
        l=float(input('ingre el valor de uno de los lados del rombo'))
        print('el perimetro del rombo es:')
        print(rombo(l))
    case '6':
        l=float(input('ingrese el valor del lado del trapecio'))
        b=float(input('ingre la base del trapecio'))
        print('el perimetro del trapecio es:')
        print(trapecio(b+b)+(l))
    case '2':
        d=float(input('ingre el perimetro del circulo'))
        pi = 3.14
        print('el perimetro del circulo es:')
        print(circulo(pi*d))