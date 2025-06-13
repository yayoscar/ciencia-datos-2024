from matematicas_clase import promedio as prom,sumar
from entradas import input_float as e,input_entero

num1=input_entero("Dame el numero 1")
num2 =input_entero("Dame un numero 2")

num1=e("Dame el numero 1")
num2 =e("Dame un numero 2")

print(sumar(2,3))

lista = [1,2,3,4,5,6]

promedio_ = prom(lista)

print(f"el promedio de {lista} es:{promedio_}")