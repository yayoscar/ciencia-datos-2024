nombres_archivo = ['doc.txt', 'reporte.txt', 'presentacion.txt']

for nombre in nombres_archivo:
    archivo = open(nombre, "w")
    archivo.write("Hola")
    archivo.close()