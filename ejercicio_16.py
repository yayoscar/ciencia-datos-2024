import math
try:
    numero = int(input("ingresa un numero entero no negativo:"))
    if numero < 0:
        print("la factorial no esta definnida pa numeros negativos.")
    else:
        print(f"la factorial de {numero} es: {math.factorial(numero)}")
        print("por favor, ingresa un numero entero valido.")
