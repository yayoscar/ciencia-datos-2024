import random

def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])

def main():
    while True:
        resultado = lanzar_moneda()
        print(f"\nResultado del lanzamiento: {resultado}")

        respuesta = input("¿Quieres volver a lanzar la moneda? (s/n): ").strip().lower()
        if respuesta != 's':
            print("¡Hasta la próxima!")
            break

main()
