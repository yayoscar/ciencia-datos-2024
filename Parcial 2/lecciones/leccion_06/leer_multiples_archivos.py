nombres_archivos=['a.txt','b.txt','c.txt']
for nombre_archivo in nombres_archivos:
    archivos=open(nombre_archivo,'r')
    print(archivos.read())
    archivos.close()