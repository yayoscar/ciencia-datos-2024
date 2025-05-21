def litros_a_m3(litros):
    metros_cubicos = litros * 0.001
    return metros_cubicos

litros = 1000
metros_cubicos = litros_a_m3(litros)
print(f"{litros} litros son equivalentes a {metros_cubicos} metros cúbicos.")