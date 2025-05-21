try:
    valor_total = float(input("Ingresa el valor total: "))
    if valor_total == 0:
        print("No es posible dividir entre cero. Ejecuta el programa de nuevo.")
    else:
        valor = float(input("Ingresa el valor: "))
        porcentaje = (valor / valor_total) * 100
        print(f"Eso es {porcentaje:.1f}%")
except ValueError:
    print("Debes ingresar un número. Ejecuta el programa de nuevo.")