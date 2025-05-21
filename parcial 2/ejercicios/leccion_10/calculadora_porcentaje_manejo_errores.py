try:
    valor_total = float(input("Ingresa el valor total: "))
    valor = float(input("Ingresa el valor: "))
    porcentaje = valor/valor_total * 100
    print(f"el porcentaje es igual a {porcentaje}")
except ValueError:
    print("debes ingresar un numero, intenta de nuevo el programa")