import math

def menu():
    print(" CÁLCULO DE PERÍMETROS")
    print("1. Rectángulo")
    print("2. Cuadrado")
    print("3. Hexágono")
    print("4. Pentágono")
    print("5. Rombo")
    print("6. Trapecio")
    print("7. Círculo")
    print("0. Salir")

def perimetro_rectangulo():
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    return 2 * (base + altura)

def perimetro_cuadrado():
    lado = float(input("Ingrese el lado del cuadrado: "))
    return 4 * lado

def perimetro_hexagono():
    lado = float(input("Ingrese el lado del hexágono: "))
    return 6 * lado

def perimetro_pentagono():
    lado = float(input("Ingrese el lado del pentágono: "))
    return 5 * lado

def perimetro_rombo():
    lado = float(input("Ingrese el lado del rombo: "))
    return 4 * lado

def perimetro_trapecio():
    lado1 = float(input("Ingrese la base mayor: "))
    lado2 = float(input("Ingrese la base menor: "))
    lado3 = float(input("Ingrese el lado no paralelo 1: "))
    lado4 = float(input("Ingrese el lado no paralelo 2: "))
    return lado1 + lado2 + lado3 + lado4

def perimetro_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    return 2 * math.pi * radio

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            print(f"Perímetro del rectángulo: {perimetro_rectangulo():.2f}")
        elif opcion == "2":
            print(f"Perímetro del cuadrado: {perimetro_cuadrado():.2f}")
        elif opcion == "3":
            print(f"Perímetro del hexágono: {perimetro_hexagono():.2f}")
        elif opcion == "4":
            print(f"Perímetro del pentágono: {perimetro_pentagono():.2f}")
        elif opcion == "5":
            print(f"Perímetro del rombo: {perimetro_rombo():.2f}")
        elif opcion == "6":
            print(f"Perímetro del trapecio: {perimetro_trapecio():.2f}")
        elif opcion == "7":
            print(f"Perímetro del círculo: {perimetro_circulo():.2f}")
        elif opcion == "0":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
