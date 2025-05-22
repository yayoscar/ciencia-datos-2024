def litros_a_m3(litros):
    metros_cubicos = litros / 1000
    return metros_cubicos
def main():
    try:
        litros = float(input("ingresa la cantidad de litros para convertirlo a metros cubicos"))
        metros_cubicos = litros_a_m3(litros)
        print(f"{litros} son iguales a {metros_cubicos} metros cubicos")
    except ValueError:
        print("ingrese un valor valido")

if __name__ == "__main__":
    main()