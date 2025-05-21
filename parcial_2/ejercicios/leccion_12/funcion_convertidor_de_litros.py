def litros_a_m3(litros):
    resultado = litros/1000
    return resultado
litros = int(input("Ingresa la cantidad de litros y lo convertiré a metros cúbicos: "))
print("Eso son:", litros_a_m3(litros), "m3")