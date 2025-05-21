def obtener_tamperaturas():
    with open('archivos/data.txt') as archivo:
        data = archivo.readlines()
    del data[0]
    data = [float(item) for item in data]
    return data

temperaturas = obtener_tamperaturas()
print(temperaturas)