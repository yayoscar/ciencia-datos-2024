try:
    valor_total = float(input("Ingresa el valor total: "))
    valor = float(input("Ingresa el valor: "))
    porcentaje = valor/valor_total * 100
    print(f"Eso es {porcentaje}%")
except ValueError:
    print("Ingresa un número y ejecuta el programa de nuevo")
except ZeroDivisionError:
    print("Tu valor total no puede ser 0")