salario = float(input("Ingrese el salario actual: "))
incremento = float(input("Ingrese el porcentaje de incremento (ej. 10 para 10%): "))

nuevo_salario = salario + (salario * incremento / 100)

print(f"El nuevo salario es: ${nuevo_salario:.2f}")
