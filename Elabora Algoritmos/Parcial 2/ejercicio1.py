def imc(peso,estatura):
    imc = peso/(estatura **2)
    return imc
peso = 48
estatura = 1.50
resultado = imc(peso,estatura)
print("El IMC es", resultado)
