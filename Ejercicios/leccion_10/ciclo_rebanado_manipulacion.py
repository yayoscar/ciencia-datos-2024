archivos = ["reporte.txt", "descargas.txt", "exito.txt", "carpetas.txt"]

for archivo in archivos:
    nombre_sin_extension = archivo.split(".")[0].capitalize()
    print(nombre_sin_extension)
