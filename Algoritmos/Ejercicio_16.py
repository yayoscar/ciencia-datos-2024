import math

try:
 numero = int(input("ingrese un numero que no sea negativo: "))
 if numero < 0:
     print("La factorial no funciona en numeros negativos")
 else:
     print(f"la factorial de {numero} es: {math.factorial(numero)}")
except ValueError:
    print("Ingresa un numero entero valido")