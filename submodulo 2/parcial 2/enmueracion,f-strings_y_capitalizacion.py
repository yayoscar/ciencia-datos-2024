nombre_archivos = ['documento','informe','presentacion']
for indice, nombre_archivos in enumerate (nombre_archivos) :
    nombre_archivos = nombre_archivos.capitalize()
    print(f"{indice}-{nombre_archivos}.txt")