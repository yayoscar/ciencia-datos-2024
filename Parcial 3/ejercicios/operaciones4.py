import matematicas as mat

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
op = input("¿Qué operación deseas hacer? (sumar, restar, multiplicar, dividir): ")

if op == "sumar":
    print("Resultado:", mat.sumar(num1, num2))
elif op == "restar":
    print("Resultado:", mat.restar(num1, num2))
elif op == "multiplicar":
    print("Resultado:", mat.multiplicar(num1, num2))
elif op == "dividir":
    print("Resultado:", mat.dividir(num1, num2))
else:
    print("Operación no válida")