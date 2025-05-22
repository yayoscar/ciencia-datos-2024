try:
    valor_total = float(input("ingrese el valor total: "))
    valor = float(input("Ingrese el valor: "))
    porcentaje = valor/valor_total * 100
    print(f"eso es {porcentaje}%")
except ValueError:
    print("Deebes ingresar un numero, ejecute denuevo el programa")
except ZeroDivisionError:
    print("tu valor total no puede ser cero")