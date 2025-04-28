with open('parrafo.txt', 'w', encoding='utf-8') as archivo:
    archivo.write("Esta es la primera línea.\n")
    archivo.write("Aquí tenemos la segunda línea.\n")
    archivo.write("Y finalmente la tercera línea.\n")

with open('parrafo.txt', 'r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()
    cantidad = len(lineas)

print(f"El archivo tiene {cantidad} líneas.")