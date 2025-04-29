numeros = [4.6, 7.5, 2.0, 5.9, 3.7]
numeros.sort()
with open("orden.txt", "w") as archivo:
    archivo.write(",".join(map(str, numeros)))
    print("Archivo orden.txt creado con éxito")