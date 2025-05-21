from logging import exception

try:
     valor_total = float(input("Ingresa el valor total: "))
     valor = float(input("Ingresa el valor: "))
     porcentaje = valor/valor_total * 100
     print(f"eso es {porcentaje}%")
except ValueError:
     print("debes ingresar un numero ingresa el programa de nuevo")