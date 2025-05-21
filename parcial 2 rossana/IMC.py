def imc(peso, estatura):
    imc= peso/estatura**2
    return imc
peso= 69
estatura= 1.70
resultado= imc(peso, estatura)
print(resultado)