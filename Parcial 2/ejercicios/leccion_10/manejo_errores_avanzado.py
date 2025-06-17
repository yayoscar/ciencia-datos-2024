try:
    valor_total = float(input("Ingresa el valor total: "))
    valor = float(input("Ingresa el valor: "))
    total = valor / valor_total * 100
    print("Eso es:", total)
except ValueError:
    print("Debes ingresar un número. Ejecuta el programa de nuevo.")
except ZeroDivisionError:
    print("Tu valor total no puede ser cero.")