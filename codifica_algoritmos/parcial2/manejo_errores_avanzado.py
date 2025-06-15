try:
    valor_total = float(input("Ingresa el valor total: "))
    valor = float(input("Ingresa el valor: "))

    if valor_total == 0:
        print("Tu valor total no puede ser cero.")
    else:
        porcentaje = (valor / valor_total) * 100
        print(f"Eso es {porcentaje:.1f}%")

except ValueError:
    print("Debes ingresar un número. Ejecuta el programa de nuevo.")