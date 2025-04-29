with open("parrafo.txt", "w") as archivo:
    archivo.write("Esta es la primera línea del archivo.\n")
    archivo.write("Aquí está la segunda línea.\n")
    archivo.write("Y finalmente, la tercera línea.\n")


    with open("parrafo.txt", "r") as archivo:
        lineas = archivo.readlines()
        cantidad_lineas = len(lineas)

    print(f"El archivo tiene {cantidad_lineas} líneas.")