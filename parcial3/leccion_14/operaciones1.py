from matematicas01 import sumar as sum
from matematicas01 import restar as rest
from matematicas01 import multiplicar as mult
from matematicas01 import dividir as div

import entradas as e

num1 = e.input_numero("Ingresa el primer numero")
num2 = e.input_numero("Ingresa el segundo numero")
operador = input("Que operacion quieres hacer? sum/rest/mult/div ")
if operador == "sum":
     print(num1 + num2)
elif operador == "rest":
    print(num1-num2)
elif operador == "mult":
    print(num1*num2)
elif operador=="div":
    print(num1*num2)
else:
    print("no entiendo esta accion")