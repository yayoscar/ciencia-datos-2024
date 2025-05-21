with open('temperaturas.txt', 'r') as archivo:
    contenido = archivo.readlines()
    promedio_de_temperaturas = len(contenido)
    print(promedio_de_temperaturas)
