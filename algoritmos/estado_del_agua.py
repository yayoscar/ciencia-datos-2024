temperatura = float(input("Ingrese la temperatura del agua: "))
if temperatura <0:
    print("El estado del agua es sólido")
elif 0 < temperatura < 100:
    print("El estado del agua es líquido")
else:
    print("Qué")