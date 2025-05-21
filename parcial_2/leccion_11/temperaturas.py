def obtener_temperaturas():
    with open("archivos/data.txt","r")as archivo:
        data = archivo.readlines()
    return data

temperaturas = obtener_temperaturas()
print(temperaturas)