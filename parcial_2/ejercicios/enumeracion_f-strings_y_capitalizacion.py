nombres_archivos = ["documento","informe","presentacion"]
for indice,nombres_archivo in enumerate(nombres_archivos):
    nombres_archivo = nombres_archivo.capitalize()
    print(f"{indice}-{nombres_archivo}.txt")
