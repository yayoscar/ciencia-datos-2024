salario_actual = float(input("ingresa el salario actual del trabajor:"))

porcentaje_incremento = float(input("ingresa el porcentaje de incremento (%):"))
incremento = salario_actual * (porcentaje_incremento / 100)
nuevo_salario = salario_actual + incremento

print(f"\nSalario actual: ${salario_actual:.2f}")
print(f"incremento aplicado: ${incremento:.2f}")
print(f"nuevo salrio: $ {nuevo_salario:.2f}")
