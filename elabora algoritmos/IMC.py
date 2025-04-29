def inc(peso, estatura):
    imc =peso/(estatura*estatura)
    return imc
peso= 45
estatura = 1.53
inc = inc(peso,estatura)
print("tu indice de masa corporal(IMC) es de",inc)