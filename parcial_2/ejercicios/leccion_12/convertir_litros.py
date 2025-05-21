def litros_a_m3(litros_locales):
    metros_locales = litros_locales / 1000
    return metros_locales
litros = int(input("Ingresa la cantidasd de litros: "))
print("Metros cúbicos: ", litros_a_m3(litros))