def inc(peso, estatura):
    n= peso/(estatura*estatura)
    return n
peso = 76
estatura = 1.75
n = inc(76,1.75)
print("su indice de masa corporal es",n)