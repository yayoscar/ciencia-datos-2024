archivos = ["reporte.txt", "descargas.txt", "exito.txt", "carpetas.txt"]

for archivo in archivos:
    nombre_sin_extension = archivo.split(".")[0]
    print(nombre_sin_extension)
