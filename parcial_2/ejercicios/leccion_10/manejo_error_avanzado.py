try:
    valor_total = float(input("Ingresa el valor total: "))
    valor = float(input("ingresa el valor: "))
    porcentaje = (valor / valor_total) * 100
    print(f"Eso es el {porcentaje}%")
except ValueError:
    print("Debes ingresar un número")
except ZeroDivisionError:
    print("Tu valor total no puede ser 0")