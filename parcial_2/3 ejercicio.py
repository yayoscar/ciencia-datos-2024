temperatura=int(input("ingrese la temperatura: "))
if temperatura<15:
    print("hace frio")
elif 15 <= temperatura <= 25:
    print("clima agradable")
else:
    print("hace calor")


    def obtener_temperaturas():
        with open("archivo/data.txt", "r") as archivo:
            data = archivo.readline()
        data = data[1:]
        data = [float(item) for item in data]
        return data


    temperaturas = obtener_temperaturas()
    print(temperaturas)
