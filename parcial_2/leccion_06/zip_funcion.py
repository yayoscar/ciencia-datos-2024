paises = ["albania", "belgica", "canada", "dinamarca", "etiopia"]
nombres_archivo = ['ap.txt', 'bp.txt', 'cp.txt', 'dp.txt', 'ep.txt']

for pais,nombre_archivo in zip(paises,nombres_archivo):
    archivo = open(nombre_archivo,"w")
    archivo.write(pais)
    archivo.close()
    