def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Ingrese un número: "))
print(f"El factorial de {num} es: {factorial(num)}")