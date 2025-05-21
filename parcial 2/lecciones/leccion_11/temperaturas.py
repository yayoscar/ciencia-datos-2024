# programa que lea las temperaturas desde un archivo data.txt y la liste
def obtener_temperaturas():
    with open("archivos/data.txt", "r") as archivo:
        data = archivo.readlines()
        data = data[1:]
        data = [float(item) for item in data]
        return data

temperatura = obtener_temperaturas()
print(temperatura)

