import operaciones1
numero1 = ("Ingrese el primer numero: ")
numero2 = ("Ingrese el segundo numero: ")
op = input("¿Qué operación desea realizar?: ")

if op == "sumar":
    resultado = op.sumar(numero1,numero2)
    return resultado

elif op == "restar":
    resultado = op.restar(numero1,numero2)
    return resultado

elif op == "divivion":
    resultado = dividir(numero1,numero2)
    return resultado


