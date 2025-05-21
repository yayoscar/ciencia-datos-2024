nombres_archivo = ['doc.txt', 'reporte.txt', 'presentacion.txt']
for nombre in nombres_archivo:
    file = open(nombre, 'w')
    file.write("Hola")
    file.close()