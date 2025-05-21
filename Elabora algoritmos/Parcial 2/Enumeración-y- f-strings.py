nombres_archivos= ["documentos", "informe", "presentacion"]
for indice, nombres_archivos in enumerate(nombres_archivos):
    nombres_archivos = nombres_archivos.capitalize()
    print(f"{indice}-{nombres_archivos}.txt")