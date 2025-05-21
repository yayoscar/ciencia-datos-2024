def calcular_nuevo_salario (salario_actual, porcentaje_incremento):
    incremento = salario_actual * (porcentaje_incremento/ 100)
    nuevo_salario = salario_actual + incremento
    return nuevo_salario

#Entrada del usuario
salario = float (input("Introduce tu salario actual: "))
incremento = float(input("Introduce el porcentaje de incremento: "))

#Resultado
nuevo_salario = calcular_nuevo_salario (salario, incremento)
print (f" Tu nuevo salario es: {nuevo_salario}")