nombre_archivos = ["a.txt","b.txt","c.txt"]
for nombre_archivos in nombre_archivos:
    archivo = open(nombre_archivos,"r")
    print(archivo.read())
    archivo.close()