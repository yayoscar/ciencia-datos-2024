nombres_archivos = ['documento', 'informe', 'presentación']
for indice,nombre_archivo in enumerate(nombres_archivos):
    nombre_archivo = nombre_archivo.capitalize()
    print(f"{indice}-{nombre_archivo}.txt")