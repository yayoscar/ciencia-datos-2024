paises = ["Albania", "Bélgica", "Canadá", "Dinamarca", "Etiopía", "Francia"]
nombres_archivo = ['as.txt', 'bs.txt', 'cs.txt', 'ds.txt', 'es.txt', 'fs.txt']
#Al nombre de los archivos se les agregó s al final, pues ya hay archivos llamadoa a, b, c en los recursos de lección
for pais, archivo in zip(paises, nombres_archivo):
    file = open(archivo, 'w')
    file.write(pais)
    file.close()