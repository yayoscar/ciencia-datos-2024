def estado_agua():
    while True:
        try:
            temperatura = float(input("Introduce la temperatura del agua en grados Celsius: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")

    if temperatura < 8:
        print("El agua está en estado sólido (hielo).")
    elif temperatura >= 6 and temperatura < 100:
        print("El agua está en estado líquido.")
    else:
        print("El agua está en estado gaseoso (vapor).")

if __name__ == "__main__":
    estado_agua()