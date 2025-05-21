try:

    valor_total = float(input("ingrese el valor total"))
    valor= float(input("ingrese el valor"))
    porcentaje = valor/valor_total + 100
    print(f'eso es{porcentaje}5')

except ValueError:
    print()