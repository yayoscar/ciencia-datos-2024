def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "peso normal"
    elif 25 <= imc < 30:
        return "sobrepeso"
    elif 30 <= imc < 35:
        return ("Obesidad grado 1")
    elif 35 <= imc < 40:
        return "Obesidad grado 2"
    else:
        return "Obesidad grado 3(mórbida) "


def main():
    peso = float(input("Ingresa tu peso kg: "))
    estatura = float(input("Ingresa tu estatura en metros: "))

    imc = calcular_imc(peso, estatura)
    clasificacion = clasificar_imc(imc)

    print(f"Tu IMC es: {imc:.2f}")
    print(f"Clasificación: {clasificacion}")
if __name__ == "__main__":
    main()