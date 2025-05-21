particulas = int(input("Ingrese la calidad del aire"))
if particulas <= 99:
    print("Bueno")
elif particulas <= 199:
    print("Regular")
elif particulas <= 299:
    print("Alerta")
elif particulas <= 499:
    print("Premergencia")
else:
    print("Emergencia")