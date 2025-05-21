def nuevo_salario(salario_incremento):
    incremento = salario_actual * (incremento_porcentaje / 100)
    nuevo_salario = salario_actual + incremento
    return nuevo_salario

salario_actual = float(input("Ingresa el salario actual: "))
incremento_porcentaje = float(input("Ingresa el porcentaje de incremento (%): "))

salario = salario_actual * incremento_porcentaje
print(f"El nuevo salario es: ${nuevo_salario:.2f}")
print("salario actual")
print("porcentaje de incremento")