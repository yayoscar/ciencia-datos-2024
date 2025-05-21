def interpretar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidad grado I"
    elif 35 <= imc < 39.9:
        return "Obesidad grado II"
    else:
        return "Obesidad grado III"

def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)

try:
    peso = float(input("Ingresa tu peso en kilogramos: "))
    estatura = float(input("Ingresa tu estatura en metros (ej. 1.75): "))

    resultado = calcular_imc(peso, estatura)
    categoria = interpretar_imc(resultado)

    print("\n--- Resultado ---")
    print("Tu IMC es:", round(resultado, 2))
    print("Clasificación:", categoria)
except ValueError:
    print("Por favor ingresa números válidos.")