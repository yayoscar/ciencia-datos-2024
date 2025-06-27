def calcular_interes_simple(capital, tasa, tiempo):
    interes = capital * (tasa / 100) * tiempo
    monto_total = capital + interes
    return interes, monto_total

def calcular_interes_compuesto(capital, tasa, tiempo):
    monto_total = capital * ((1 + (tasa / 100)) ** tiempo)
    interes = monto_total - capital
    return interes, monto_total

def main():
    while True:
        print("\n--- CALCULADORA DE INTERÉS ---")
        print("1. Calcular Interés Simple")
        print("2. Calcular Interés Compuesto")
        print("3. Salir")
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "3":
            print("¡Gracias por usar la calculadora!")
            break
        elif opcion not in ["1", "2"]:
            print("Opción no válida.")
            continue

        try:
            capital = float(input("Ingresa el capital (dinero inicial): "))
            tasa = float(input("Ingresa la tasa de interés (%): "))
            tiempo = float(input("Ingresa el tiempo (en años): "))
        except ValueError:
            print("Por favor, ingresa solo números.")
            continue

        if opcion == "1":
            interes, total = calcular_interes_simple(capital, tasa, tiempo)
            print(f"Interés ganado (simple): ${interes:.2f}")
            print(f"Monto total: ${total:.2f}")
        elif opcion == "2":
            interes, total = calcular_interes_compuesto(capital, tasa, tiempo)
            print(f"Interés ganado (compuesto): ${interes:.2f}")
            print(f"Monto total: ${total:.2f}")

        seguir = input("¿Deseas hacer otro cálculo? (s/n): ").lower()
        if seguir != "s":
            break

if __name__ == "__main__":
    main()
