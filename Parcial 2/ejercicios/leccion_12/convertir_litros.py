def litros_a_m3():
    metros_cubicos = litros / 1000
    return metros_cubicos

litros = float(input("Ingrese los litros: "))
metros_cubicos = litros_a_m3()
print(f"{litros} es equivalente a {metros_cubicos}")
