def obtener_temperaturas():
    with open("archivo/data.txt","r") as archivo:
        data = archivo.readline()
    data = data[1:]
    data = [float(item) for item in data]
    return data


    
temperaturas = obtener_temperaturas()
print(temperaturas)
