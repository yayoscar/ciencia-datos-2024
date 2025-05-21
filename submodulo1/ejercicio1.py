def imc(peso, estatura):
    imc = peso / (estatura **2)
    return imc
peso = 80
estatura = 1.80
resultado = imc(peso, estatura)
print("El imc es: ",resultado)