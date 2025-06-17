def menu():
    print("\n--- MENÚ ---")
    print("1. Rectángulo")
    print("2. Cuadrado")
    print("3. Hexágono")
    print("4. Pentágono")
    print("5. Rombo")
    print("6. Trapecio")
    print("7. Círculo")
    print("8. Salir")

def perimetro_rectangulo(b, h):
    return 2 * (b + h)

def perimetro_cuadrado(lado):
    return 4 * lado

def perimetro_hexagono(lado):
    return 6 * lado

def perimetro_pentagono(lado):
    return 5 * lado

def perimetro_rombo(lado):
    return 4 * lado

def perimetro_trapecio(base_mayor, base_menor, lado1, lado2):
    return base_mayor + base_menor + lado1 + lado2

def perimetro_circulo(pi, d):
    return pi * d

def main():
    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            b = float(input("Base del rectángulo: "))
            h = float(input("Altura del rectángulo: "))
            print(f"Perímetro del rectángulo: {perimetro_rectangulo(b, h)}")
        elif opcion == "2":
            lado = float(input("Lado del cuadrado: "))
            print(f"Perímetro del cuadrado: {perimetro_cuadrado(lado)}")
        elif opcion == "3":
            lado = float(input("Lado del hexágono: "))
            print(f"Perímetro del hexágono: {perimetro_hexagono(lado)}")
        elif opcion == "4":
            lado = float(input("Lado del pentágono: "))
            print(f"Perímetro del pentágono: {perimetro_pentagono(lado)}")
        elif opcion == "5":
            lado = float(input("Lado del rombo: "))
            print(f"Perímetro del rombo: {perimetro_rombo(lado)}")
        elif opcion == "6":
            base_mayor = float(input("Base mayor del trapecio: "))
            base_menor = float(input("Base menor del trapecio: "))
            lado1 = float(input("Lado 1 del trapecio: "))
            lado2 = float(input("Lado 2 del trapecio: "))
            print(f"Perímetro del trapecio: {perimetro_trapecio(base_mayor, base_menor, lado1, lado2)}")
        elif opcion == "7":
            d = float(input("Diámetro del círculo: "))
            print(f"Perímetro del círculo: {perimetro_circulo(3.1416, d)}")
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()