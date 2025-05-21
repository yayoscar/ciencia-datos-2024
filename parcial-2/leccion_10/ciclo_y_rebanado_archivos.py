archivos = ["reporte.txt", "descargas.txt", "exito.txt", "carpetas.txt"]
for archivo in archivos:
    nombres_sin_archivo = archivo[:-4]
    print(nombres_sin_archivo)