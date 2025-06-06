#import matematicas
#from matematicas import sumar,promedio
import matematicas as mat
import entradas as e
num1 = e.input_float("Dame el número 1: ")
num2 = e.input_float("Dame el número 2: ")
print(mat.sumar(num1,num2))
print(mat.promedio([1,2,3,4,5,6,7,8]))
