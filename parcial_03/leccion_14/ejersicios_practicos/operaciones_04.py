import matematicas_02 as mat

print("Elige una operación: sumar, restar, multiplicar, dividir")
operacion = input("Operación: ").lower()

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

if operacion == "sumar":
    print("Resultado:", mat.sumar(a, b))
elif operacion == "restar":
    print("Resultado:", mat.restar(a, b))
elif operacion == "multiplicar":
    print("Resultado:", mat.multiplicar(a, b))
elif operacion == "dividir":
    print("Resultado:", mat.dividir(a, b))
else:
    print("Operación no válida.")