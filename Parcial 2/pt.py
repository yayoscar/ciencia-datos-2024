def elevar_al_cubo(numero):
    return numero ** 3


def main():
    continuar = "s"
    while continuar.lower() == "s":
        try:
            numero = float(input("Ingrese un número: "))
            resultado = elevar_al_cubo(numero)
            print(f"El cubo de {numero} es {resultado}")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

        continuar = input("¿Desea continuar? (s/n): ")
        while continuar.lower() not in ["s", "n"]:
            continuar = input("Respuesta inválida. Por favor, ingrese 's' para sí o 'n' para no: ")

    print("Programa terminado.")


if _name_ == "_main_":
    main()