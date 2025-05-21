archivos = ["reporte.txt","descargas.txt","éxito.txt","carpetas.txt"]
for archivo in archivos:
    indice = archivo.index('.')
    print(archivo[:indice])