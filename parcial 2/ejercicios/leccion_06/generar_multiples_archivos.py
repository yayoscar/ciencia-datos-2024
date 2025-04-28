nombre_archivos=["doc,txt","reporte.txt","presentaciopnes.txt"]
for nombre_archivos in nombre_archivos:
    archivo=open(nombre_archivos,"a")
    archivo.write("hola")
    archivo.close()