def calcular_nuevo_salario(salario_actual, incremento_percent):

    incremento_decimal = incremento_percent / 100
    nuevo_salario = salario_actual + (salario_actual * incremento_decimal)
    return nuevo_salario

try:
    salario = float(input("Introduce tu salario actual: "))
    incremento = float(input("Introduce el porcentaje de incremento (%): "))

    nuevo_salario = calcular_nuevo_salario(salario, incremento)
    print(f"Tu nuevo salario será: ${nuevo_salario:.2f}")
except ValueError:
    print("Por favor, introduce valores numéricos válidos.")