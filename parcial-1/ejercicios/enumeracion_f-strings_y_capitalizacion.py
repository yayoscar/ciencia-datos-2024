
nombre_archivos = ['documentp','informe','presentacion']
for datos, nombre_archivos in enumerate(nombre_archivos):
    nombre_archivos = nombre_archivos.capitalize()
    print(f"{datos}-{nombre_archivos}.txt")