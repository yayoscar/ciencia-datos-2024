
nombres_archivo = ['doc.txt', 'reporte.txt', 'presentacion.txt']
for archivo in nombres_archivo:
    with open(archivo, "w", ) as f:
        f.write("Hola")
