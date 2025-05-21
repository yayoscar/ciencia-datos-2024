import math

try:
    numero = int(input("ingresa un numero entero no negativo:"))
    if numero < 0:
        print("la factorial no esta definida para numeros negativos.")
    else:
        print(f"la factorial de un numero es:{math.factorial(numero)}")
except ValueError:
    print("favor de ingresar un numero entero valido")