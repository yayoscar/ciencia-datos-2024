def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def interpretar_imc(imc):
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
        peso = float(input("Ingresa tu peso en kg: "))
        altura = float(input("Ingresa tu altura en metros: "))
        imc = calcular_imc(peso, altura)
        categoria = interpretar_imc(imc)
        print(f"Tu IMC es: {imc:.2f} ({categoria})")
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")

if __name__ == "__main__":
    main()
