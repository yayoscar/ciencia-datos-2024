def formatear_nombre_archivo():
    nombre_archivo = "reporte.txt"
    nombre_modificado = nombre_archivo[:-4].capitalize()
    return nombre_modificado

print(formatear_nombre_archivo())