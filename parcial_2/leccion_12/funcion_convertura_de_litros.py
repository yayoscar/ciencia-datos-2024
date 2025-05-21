def litros_a_m3(litros):
    return  litros / 1000

litros = float(input("ingrese la cantidad de litros: "))
resultado = litros_a_m3(litros)
print(f"{litros} litros son {resultado} metros cubicos")
