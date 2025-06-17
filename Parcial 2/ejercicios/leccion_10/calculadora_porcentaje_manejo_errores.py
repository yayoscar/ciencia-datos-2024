try:
    valor_total = float(input("Ingresa el valor total: "))
    valor = float(input("Ingresa el valor: "))
    total = valor / valor_total * 100
    print(f"Eso es: {total}%")
except ValueError:
    print("Debes ingresar un número. Ejecuta el programa de nuevo.")