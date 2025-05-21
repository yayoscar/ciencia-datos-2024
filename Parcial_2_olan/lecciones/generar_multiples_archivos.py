nombres_archivo = ['doc.txt', 'reporte.txt', 'presentacion.txt']

with open('nombres_archivo.txt', 'w', encoding='utf-8') as archivo:
    for nombre in nombres_archivo:
        archivo.write(nombre + '\n')