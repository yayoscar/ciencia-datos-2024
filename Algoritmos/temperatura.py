temperatura = int(input("cual es la temperatura del agua?: "))

if temperatura < 0:
    print("el agua esta congelada")
elif temperatura > 0 and temperatura < 100:
    print("el agua esta liquida")
else:
    print("el agua es vapor")