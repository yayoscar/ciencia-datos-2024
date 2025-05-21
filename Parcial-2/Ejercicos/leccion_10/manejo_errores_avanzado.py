try:
    valor_total = float(input("ingresa el valor total:  "))
    valor = float(input("ingresa el valor:  "))
    porcentaje = valor/valor_total *100
    print(f"Eso es {porcentaje}%")
except ValueError:
    print("Debes ingresar un numero. Ejecuta el programa")
except ZeroDivisionError:
    print("Tu valor total no puede ser cero")