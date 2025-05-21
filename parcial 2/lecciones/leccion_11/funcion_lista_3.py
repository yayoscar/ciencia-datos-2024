def formatear_nombre_archivo():
    nombre_archivo = "reporte.txt"
    nombre_archivo = nombre_archivo [1:4]
    nombre_archivo = nombre_archivo.capitalize()
    return nombre_archivo

print(formatear_nombre_archivo())