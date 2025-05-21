nombres_archivo = ['doc.txt', 'reporte.txt', 'presentacion.txt']
for texto in nombres_archivo:
    archivo = open(texto, 'w')
    archivo.write("Hola")
    archivo.close()