nombres_archivos= ["a.txt","b.txt","c.txt"]
for nombres_archivos in nombres_archivos:
    archivo=open(nombres_archivos,"r")
    print(archivo.read())
    archivo.close()
    