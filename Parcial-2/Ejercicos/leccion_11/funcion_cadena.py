def formatear_nombre_archivo():
    nombre_archivo = "reporte.txt"
    nombre_archivo = nombre_archivo [:-4]
    nombre_archivo = nombre_archivo.capitalize()

mensaje = formatear_nombre_archivo()
print(mensaje)