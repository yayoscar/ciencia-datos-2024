def litros_a_m3(litros):
    metros_cubicos = litros / 1000
    return metros_cubicos

# Ejemplo de uso
litros = 5000
m3 = litros_a_m3(litros)
print(f"{litros} litros son {m3} metros cúbicos")