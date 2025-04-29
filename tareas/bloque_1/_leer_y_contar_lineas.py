with open("parrafo.txt", "w") as archivo:
    archivo.write("Esto es una línea de ejemplo.\n")
    archivo.write("Aquí va otra línea más.\n")
    archivo.write("Y esta es la tercera línea del texto.\n")


with open("parrafo.txt", "r") as archivo:
    lineas = archivo.readlines()
    numero_de_lineas = len(lineas)

print(f"El archivo tiene {numero_de_lineas} líneas.")
