nombres_archivo = ['doc.txt', 'reporte.txt', 'presentacion.txt']
for nombre,archivo in nombres_archivo:
    archivo = open(nombres_archivo,"w")
    archivo.write("Hola")
    archivo.close()