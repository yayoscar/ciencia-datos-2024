with open("parrafo.txt", "r") as archivo:
    lineas = archivo.readlines()
print(f"el archivo tiene{len(lineas)} lineas.")