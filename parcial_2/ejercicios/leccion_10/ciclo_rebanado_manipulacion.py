archivos = ["reporte.txt", "descargas.txt", "exito.txt", "carpetas.txt"]

for archivo in archivos:
    nombre = archivo[:-4].capitalize()
    print(nombre)