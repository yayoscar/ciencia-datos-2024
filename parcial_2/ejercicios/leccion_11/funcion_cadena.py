def formatear_nombre_archivo():
    nombre_archivo = "reporte.txt"
    nombre_archivo = nombre_archivo[:7]
    return nombre_archivo
print(formatear_nombre_archivo().capitalize())