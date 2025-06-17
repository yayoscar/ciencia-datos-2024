def calcular_interes_simple(capital, tasa, tiempo):
    interes = capital * tasa * tiempo
    return interes

def calcular_interes_compuesto(capital, tasa, tiempo):
    monto_final = capital
    for _ in range(tiempo):
        monto_final += monto_final * tasa
    return monto_final

def calcular_interes():
    print("Bienvenido al calculador de intereses")

    capital = float(input("Ingrese el capital inicial: "))
    tasa = float(input("Ingrese la tasa de interés anual (en %): ")) / 100
    tiempo = int(input("Ingrese el tiempo en años: "))
    tipo = input("¿Desea calcular simple o compuesto? ").strip().lower()

    if tipo == "simple":
        interes = calcular_interes_simple(capital, tasa, tiempo)
        monto = capital + interes
        print(f"Interés simple: {interes:.2f}")
        print(f"Monto total al final del periodo: {monto:.2f}")

    elif tipo == "compuesto":
        monto = calcular_interes_compuesto(capital, tasa, tiempo)
        interes = monto - capital
        print(f"Interés compuesto: {interes:.2f}")
        print(f"Monto total al final del periodo: {monto:.2f}")

    else:
        print("Opción inválida. Debe ser 'simple' o 'compuesto'.")

calcular_interes()