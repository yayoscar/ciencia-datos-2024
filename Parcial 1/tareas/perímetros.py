import math

def perimetro_cuadrado(lado):
    return 4 * lado

def perimetro_rectangulo(base, altura):
    return 2 * (base + altura)

def perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

def perimetro_circulo(radio):
    return 2 * math.pi * radio

def menu():
    print("=== CÁLCULO DE PERÍMETROS ===")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Triángulo")
    print("4. Círculo")
    print("5. Salir")

def main():
    while True:
        menu()
        opcion = input("Elige una figura (1-5): ")

        if opcion == '1':
            lado = float(input("Ingresa el lado del cuadrado: "))
            print(f"Perímetro del cuadrado: {perimetro_cuadrado(lado)}\n")

        elif opcion == '2':
            base = float(input("Ingresa la base del rectángulo: "))
            altura = float(input("Ingresa la altura del rectángulo: "))
            print(f"Perímetro del rectángulo: {perimetro_rectangulo(base, altura)}\n")

        elif opcion == '3':
            lado1 = float(input("Ingresa el primer lado del triángulo: "))
            lado2 = float(input("Ingresa el segundo lado del triángulo: "))
            lado3 = float(input("Ingresa el tercer lado del triángulo: "))
            print(f"Perímetro del triángulo: {perimetro_triangulo(lado1, lado2, lado3)}\n")

        elif opcion == '4':
            radio = float(input("Ingresa el radio del círculo: "))
            print(f"Perímetro (circunferencia) del círculo: {perimetro_circulo(radio):.2f}\n")

        elif opcion == '5':
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intenta de nuevo.\n")

# Ejecutar el programa
if __name__ == "__main__":
    main()
