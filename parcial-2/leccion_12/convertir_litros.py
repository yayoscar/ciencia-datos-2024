def litros_a_m3 (litros):
    metros_cubicos = litros/1000
    return metros_cubicos

L = float(input("introduce tu valor de litros: "))
print(litros_a_m3(L))