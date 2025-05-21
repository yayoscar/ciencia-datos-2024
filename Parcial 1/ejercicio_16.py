import math

try:
    numero = int(input("Ingrese un número cualquiera: "))
    if numero < 0:
        print("No funciona en números negativos")
    else:
        print(f"la factorial de {numero} es: {math.factorial(numero)}")
except ValueError:
    print("No valido")