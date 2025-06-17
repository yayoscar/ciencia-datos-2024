from entradas import input_int, input_float
from matematicas import sumar, restar, multiplicar, dividir
import avanzado as av
ope = input_int("""¿Qué operación quieres hacer?
1.Suma
2.Resta
3.Multiplicación
4.División
Inserta el número: """)
match ope:
    case 1:
        num1 = input_float("Inserta el número 1: ")
        num2 = input_float("Inserta el número 2: ")
        print(sumar(num1, num2))
    case 2:
        num1 = input_float("Inserta el número 1: ")
        num2 = input_float("Inserta el número 2: ")
        print(restar(num1, num2))
    case 3:
        num1 = input_float("Inserta el número 1: ")
        num2 = input_float("Inserta el número 2: ")
        print(multiplicar(num1, num2))
    case 4:
        num1 = input_float("Inserta el número 1: ")
        num2 = input_float("Inserta el número 2: ")
        print(dividir(num1, num2))
