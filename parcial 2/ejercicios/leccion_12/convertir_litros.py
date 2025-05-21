def litros_a_m3(litros):
    litros = float(input("ingresa el numero de litros: "))
    metros_cubicos = litros/1000
    return metros_cubicos

print(litros_a_m3(10000))
