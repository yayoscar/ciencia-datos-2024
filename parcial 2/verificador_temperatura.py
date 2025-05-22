def verificar_temperatura(temp):
    if temp > 7:
        return "Cálido"
    else:
        return "Frío"


print(verificar_temperatura(10))