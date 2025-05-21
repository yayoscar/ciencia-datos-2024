try:
    valor_total = float(input("Ingresa el valor total: "))
    valor = float(input("Ingresa el valor: "))
    calculo = valor/valor_total * 100
    print("el porcentaje es",calculo,"%")
except ValueError:
    print("Error:Ejecute el programa de nuevo y ingrese un numero")
except ZeroDivisionError:
    print("su valor no puede ser cero, por favor ejecute el programa de nuevo")