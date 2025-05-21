def calcular_imc(peso, estatura):
    imc = peso / estatura ** 2
    return imc

peso = 56.55
estatura = 1.70
imc= calcular_imc(peso, estatura)
print(f"El imc es: {imc}")