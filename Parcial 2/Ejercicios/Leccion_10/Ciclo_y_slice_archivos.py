archivos = ["reporte.txt", "descargas.txt", "exito.txt", "carpetas.txt"]

for archivo in archivos:
    indice=archivo.index('.')
    print(archivo[:indice])