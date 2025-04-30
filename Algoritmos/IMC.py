def imc(peso,estatura):
    imc = peso/(estatura * estatura)
    return imc
peso=60
estatura=1.60
resultado= imc(peso,estatura)

print("tu resultado es", resultado)