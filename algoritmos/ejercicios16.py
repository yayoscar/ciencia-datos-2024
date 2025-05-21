import math

try:
    numero = int(input("Ingresa un número entero no negativo: "))
    if numero < 0:
        print("La factorial no está definidia para números negativos.")
    else:
        print(f"La factorial de {numero} es: {math.factorial(numero)}")

except ValueError:
    print("Favor de ingresar un número entero válido. ")