paises = ("Albania", "Bélgica", "Canadá", "Dinamarca", "Etiopía")
nombres_archivo = ['ap.txt', 'bp.txt', 'cp.txt', 'dp.txt', 'ep.txt']

for país,nombre_archivo in zip(paises,nombres_archivo):
    archivo = open(nombre_archivo,"w")
    archivo.write(país)
    archivo.close()
