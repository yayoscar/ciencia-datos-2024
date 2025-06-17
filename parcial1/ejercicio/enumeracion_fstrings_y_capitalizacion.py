nombres_archivos = ['documento','informe', 'presentacion']
for indice,nombres_archivos in enumerate(nombres_archivos):
    nombre_archivo = nombres_archivos.capitalize()
    print(f"{indice}{nombre_archivo}.txt")