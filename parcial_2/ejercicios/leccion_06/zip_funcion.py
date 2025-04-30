paises=["albania", "belgica", "canada", "dinamarca", "etiopia", "francia"]
nombres_archivo =["albania.txt", "belgica.txt", "canada.txt", "dinamarca.txt", "etiopia.txt", "francia.txt"]
for pais,nombre_archivo in zip(paises,nombres_archivo):
    archivo=open(nombre_archivo, "w")
    archivo.write(pais)
    archivo.close()
