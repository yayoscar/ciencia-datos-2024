def calcular_nuevo_salario(salario_actual, porcentaje_incrementado):
    incremento= salario_actual*(porcentaje_incrementado/100)
    nuevo_salario=salario_actual+incremento
    return nuevo_salario
salario=float(input("ingresa tu salario actual: w"))
incremento_porcentaje=float(input("ingrese el porcentaje de incremento (%)"))
nuevo_salario= calcular_nuevo_salario(salario,incremento_porcentaje)
print(f"Tu nuevo salario es: ${nuevo_salario:.2f}")