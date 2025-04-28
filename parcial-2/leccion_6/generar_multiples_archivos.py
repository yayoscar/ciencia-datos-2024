nombres_archivo = ['doc.txt', 'reporte.txt', 'presentacion.txt']
for nombre_archivo in nombres_archivo:
    archivo = open(nombre_archivo, "w")
    archivo.write("Hola")
    archivo.close()
