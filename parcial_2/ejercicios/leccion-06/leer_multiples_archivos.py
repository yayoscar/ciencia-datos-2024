nombres_archivos = ["a.txt", "b.txt", "c.txt"]
for nombre_archivo in nombres_archivos:
    archivo = open(nombre_archivo, "r")
    print(archivo.read())
    archivo.close()