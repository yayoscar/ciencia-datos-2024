def calcular_imc(peso, estatura):
    imc = peso / (estatura ** 2)
    return imc

peso = float(input("Ingrese su peso en kilogramos: "))
estatura = float(input("Ingrese su estatura en metros: "))

imc = calcular_imc(peso, estatura)
imc = peso / (estatura**2)
print("Tu imc es de ",imc)











