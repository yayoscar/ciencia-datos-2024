nombres_archivos = ['documento', 'informe', 'presentacion']
for nombres_archivos, nombres_archivo in enumerate(nombres_archivos):
    nombres_archivo = nombres_archivo.capitalize()
    print(f"{nombres_archivos}-{nombres_archivo}.txt")