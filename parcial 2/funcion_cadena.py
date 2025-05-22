def formatear_nombre_archivo():
    nombre_archivo = "reporte.txt"
    nombre_sin_extension = nombre_archivo[:-4]
    return nombre_sin_extension.capitalize()

print(formatear_nombre_archivo())
