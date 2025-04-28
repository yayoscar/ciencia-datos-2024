paises = ["albania", "belgica", "canada", "dinamarca", "etiopoia", "franciaa"]
nombres_archivo = ['a.tx', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']
for pais,nombre_archivo in zip(paises, nombres_archivo):
    archivo = open(nombre_archivo, 'w')
    archivo.write(pais)
    archivo.close()