from matematicas import promedio as prom,sumar
import entradas as e

num1=e.input_float("dame el numero 1")
num2=e.input_float("dame el numero 2")
print(sumar(num1, num2))

lista=[1,2,3,4,5,6]

promedio = prom(lista)
print(promedio)