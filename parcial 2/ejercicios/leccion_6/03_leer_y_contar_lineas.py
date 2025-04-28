
with open("parrafo.txt", "w") as archivo:
    archivo.write("Esta es la primera línea del texto.\n")
    archivo.write("Aquí tienes la segunda línea con más contenido.\n")
    archivo.write("Y esta es la tercera línea, para terminar.\n")


with open("parrafo.txt", "r") as archivo:
    lineas = archivo.readlines()
    cantidad_lineas = len(lineas)


print(f"El archivo tiene {cantidad_lineas} líneas.")