with open('parrafo.txt', 'w') as archivo:
    archivo.write('Esta es la primera línea.\n')
    archivo.write('Aquí viene la segunda línea.\n')
    archivo.write('Finalmente, esta es la tercera línea.\n')
with open('parrafo.txt', 'r') as archivo:
    lineas = archivo.readlines()
    cantidad_lineas = len(lineas)
print(f"El archivo tiene {cantidad_lineas} líneas.")
