def formatear_nombre_archivo():
    nombre_archivo = "reporte.txt"
    nombre_archivo = nombre_archivo[:-4].capitalize()
    return nombre_archivo
print(formatear_nombre_archivo())