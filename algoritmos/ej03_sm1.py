def calcular_nuevo_salario(salario_actual, incremento_pct):
    incremento = salario_actual * (incremento_pct / 100)
    return salario_actual + incremento

def main():
    salario = float(input("Ingresa el salario actual: "))
    porcentaje = float(input("Ingresa el porcentaje de incremento: "))

    nuevo_salario = calcular_nuevo_salario(salario, porcentaje)

    print(f"El nuevo salario es: ${nuevo_salario:.2f}")

if __name__ == "__main__":
    main()