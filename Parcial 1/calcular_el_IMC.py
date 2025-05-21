def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"


def main():
    print("Calculadora de IMC")
    try:
        peso = float(input("Introduce tu peso en kilogramos (kg): "))
        altura = float(input("Introduce tu altura en metros (m): "))

        if peso <= 0 or altura <= 0:
            print("Por favor, introduce valores mayores a cero.")
            return

        imc = calcular_imc(peso, altura)
        nivel = clasificar_imc(imc)

        print(f"\nTu IMC es: {imc:.2f}")
        print(f"Clasificación: {nivel}")

    except ValueError:
        print("Error: introduce un número válido.")


if __name__ == "__main__":
    main()
