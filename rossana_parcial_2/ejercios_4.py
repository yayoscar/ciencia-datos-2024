def calcular_imc (peso, estatura):
    imc = peso / (estatura**2)
    return imc
peso = float(input("ingresa tu peso en kilogramos:"))
estatura = float(input("ingresa tu estatura en metros:"))
imc = calcular_imc(peso, estatura)
print(f"\nTu imc es: {imc:.2}")