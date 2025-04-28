nombres_archivos = ['doc.txt', 'reporte.txt', 'presentación.txt']
for nombre_archivo in nombres_archivos:
    archivo = open(nombre_archivo,"w")
    archivo.write("hola")
    archivo.close()