import operaciones

print("1-Sumar")
print("2-Restar")
print("3-Multiplicar")
print("4-Dividir")

operaciones = input("¿Qué operación deseas realizar?")

num1 = input("Ingresa el primer número: ")
num2 = input("Ingrese el segundo número: ")

if operaciones == "sumar":
    resultado = operaciones.sumar(num1,num2)

elif operaciones == "restar":
    resultado = operaciones.restar(num1,num2)

elif operaciones == "multiplicar":
    resultado = operaciones.multiplicar(num1,num2)

elif operaciones == "dividir":
    resultado = operaciones.dividir(num1,num2)

else:
     resultado = "Operación no válida"

print("El resultado de tu operacion es:", resultado)
