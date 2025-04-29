def crear_y_contar_lineas():
    # Crear un archivo con al menos 3 líneas de texto
    with open("parrafo.txt", "w") as archivo:
        archivo.write("Esta es la primera línea del párrafo.\n")
        archivo.write("Aquí va la segunda línea con más texto.\n")
        archivo.write("Y esta es la tercera línea.\n")

    # Leer el archivo y contar las líneas
    with open("parrafo.txt", "r") as archivo:
        lineas = archivo.readlines()
        cantidad = len(lineas)

    # Imprimir el resultado
    print(f"El archivo tiene {cantidad} líneas.")

# Ejecutar función
crear_y_contar_lineas()
