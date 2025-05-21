def rectangulo(b, h):
    perimetro = 2 * (b + h)
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

def trapecio(b, l):
    perimetro = (2 * b) + (2 * l)
    return perimetro

def circulo(d):
    pi = 3.14
    perimetro = pi * d
    return perimetro

print('1. Rectángulo')
print('2. Cuadrado')
print('3. Hexágono')
print('4. Pentágono')
print('5. Rombo')
print('6. Trapecio')
print('7. Círculo')

calcular = input('¿Qué perímetro deseas calcular? (1-7): ')

match calcular:
    case "1":
        b = float(input('Ingrese la base del rectángulo: '))
        h = float(input('Ingrese la altura del rectángulo: '))
        print('El perímetro del rectángulo es:', rectangulo(b, h))

    case "2":
        l = float(input('Ingrese el valor de un lado del cuadrado: '))
        print('El perímetro del cuadrado es:', cuadrado(l))

    case "3":
        l = float(input('Ingrese el valor de un lado del hexágono: '))
        print('El perímetro del hexágono es:', hexagono(l))

    case "4":
        l = float(input('Ingrese el valor de un lado del pentágono: '))
        print('El perímetro del pentágono es:', pentagono(l))

    case "5":
        l = float(input('Ingrese el valor de un lado del rombo: '))
        print('El perímetro del rombo es:', rombo(l))

    case "6":
        l = float(input('Ingrese el valor del lado del trapecio: '))
        b = float(input('Ingrese la base del trapecio: '))
        print('El perímetro del trapecio es:', trapecio(b, l))

    case "7":
        d = float(input('Ingrese el diámetro del círculo: '))
        print('El perímetro del círculo es:', circulo(d))

    case _:
        print('Opción no válida.')
