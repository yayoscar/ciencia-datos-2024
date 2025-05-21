def estado_agua(temperatura):
    if temperatura <= 0:
        return "sólido (hielo)"
    elif 0 < temperatura < 100:
        return "líquido"
    else:
        return "gaseoso (vapor)"


def main():
    print("=== ESTADO DEL AGUA SEGÚN TEMPERATURA ===")

    try:
        temp = float(input("Ingresa la temperatura en grados Celsius: "))
        estado = estado_agua(temp)
        print(f"A {temp}°C, el agua está en estado: {estado}.\n")
    except ValueError:
        print("Por favor, ingresa un número válido.")


# Ejecutar el programa
if __name__ == "__main__":
    main()
