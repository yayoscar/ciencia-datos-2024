def calcular_salario():
    print("=== calculadora de salario ===")

    precio_salario= float(input("ingrese el salario actual:"))
    incremento_porcentaje = float(input("ingrese el porcentaje de aumneto de salario:"))

    incremento = precio_salario*(incremento_porcentaje/100)
    valor_final = precio_salario*incremento
    print("\n=== resultados ===")
    print(f"salario actual: ${precio_salario:,.2f} pesos")
    print(f"incremento: ${incremento:.2f} pesos")
    print(f"valor final despues de comision:${valor_final:,.2f}pesos")
