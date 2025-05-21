def calcular_porcentaje():
    try:
        valor_total = float(input("Ingresa el valor total: "))
        if valor_total == 0:
            raise ZeroDivisionError("El valor total no puede ser cero.")

        valor = float(input("Ingresa el valor: "))
        porcentaje = (valor / valor_total) * 100
        print(f"Eso es {porcentaje:.1f}%")

    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Debes ingresar un número. Ejecuta el programa de nuevo.")

calcular_porcentaje()
