def litros_a_m3():
    litros=float(input("ingresa la cantidad de litros: "))
    metros_cubicos= litros / 1000
    return metros_cubicos

resultado= litros_a_m3()
print(f"{resultado} metros cubicos")