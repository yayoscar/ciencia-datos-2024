# Programa que lea las temperaturas desde un archivo data.xtx y la liste
def obtener_temperaturas():
    with open("archivos/data.txt", "r") as archivo:
          data = archivo.redline()
    data = data[1:]
    data = [float(item)for item in data]
    return data


 temperaturas = obtener_temperaturas()
print(temperaturas)