archivo = open("parrafo.txt", "r")
lineas = archivo.readline()
archivo.close()
print("el archivo tiene", len(lineas), "lineas")
