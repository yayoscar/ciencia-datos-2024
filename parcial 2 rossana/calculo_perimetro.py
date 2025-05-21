import math
def perimetro_rectangulo():
    base = float(input("Ingresa la base del rectángulo porfis: "))
    altura = float(input("Ingresa la altura del rectángulo porfis: "))
    return 2 * (base + altura)

def perimetro_cuadrado():
    lado = float(input("Ingresa el lado del cuadrado porfis: "))
    return 4 * lado

def perimetro_hexagono():
    lado = float(input("Ingresa el lado del hexágono porfis: "))
    return 6 * lado
def perimetro_pentagono():
    lado = float(input("Ingresa el lado del pentágono porfavor: "))
    return 5 * lado
def perimetro_rombo():
    lado = float(input("Ingresa el lado del rombo porfis: "))
    return 4 * lado
def perimetro_trapecio():
    base_mayor = float(input("Ingresa la base mayor del trapecio porfavorcito: "))
    base_menor = float(input("Ingresa la base menor del trapecio porfavor: "))
    lado1 = float(input("Ingresa el primer lado no paralelo del trapecio porfavor: "))
    lado2 = float(input("Ingresa el segundo lado no paralelo del trapecio porfissss: "))
    return base_mayor + base_menor + lado1 + lado2
def perimetro_circulo():
    radio = float(input("Ingresa el radio del círculo porfavorcitoooooo: "))
    return 2 * math.pi * radio
def menu():
    print("\nCálculo de perímetros")
    print("1.- Rectángulo")
    print("2.- Cuadrado")
    print("3.- Hexágono")
    print("4.- Pentágono")
    print("5.- Rombo")
    print("6.- Trapecio")
    print("7.- Círculo")
    print("salir")

while True:
    menu()
    opcion = input("Elige una opción del numero 1 al 7 o salir y si no me enojo 🤬): ")

    if opcion == '1':
        print("Perímetro del rectángulo:", perimetro_rectangulo())
    elif opcion == '2':
        print("Perímetro del cuadrado:", perimetro_cuadrado())
    elif opcion == '3':
        print("Perímetro del hexágono:", perimetro_hexagono())
    elif opcion == '4':
        print("Perímetro del pentágono:", perimetro_pentagono())
    elif opcion == '5':
        print("Perímetro del rombo:", perimetro_rombo())
    elif opcion == '6':
        print("Perímetro del trapecio:", perimetro_trapecio())
    elif opcion == '7':
        print("Perímetro del círculo:", perimetro_circulo())
    elif opcion == 'salir':
        print("¡Gachas por usarme te amo colazon de melon!")
        break
    elif opcion == "Salir":
        print("¡Gachas por usarme te amo colazon de melon!")
        break
    else:
        print("Ya me enoje por que pones otro numero que no sea del 1 al 7 o salir te odio a hora 🤬🤬🤬🤬🤬☠️💀.")