temperatura=int(input("ingrese la temperatura: "))
if temperatura<15:
    print("hace frio")
elif 0 <= temperatura <= 99:
    print("bueno")
elif 100 <= temperatura <= 199:
    print("regular")
elif 200 <= temperatura <= 299:
    print("alerta")
elif 300 <= temperatura <= 499:
    print("premergencia")
elif 500 <= temperatura <= 500:
    print("emergecia")