def factorial(n):
    if n < 0:
        return "error"
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
            return resultado
num = int(input("ingrese un numero: "))