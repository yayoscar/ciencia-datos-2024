paises =("Albania","Belgica","Canada","Dinamarca","Etiopia","Francia")
nombre_archivo = ["ap,txt","bp.txt","cp.txt","dp,txt","ep.txt"]

for pais, nombre_archivo in zip(paises,nombre_archivo):
    archivo = open(nombre_archivo,"w")
    archivo.write(pais)
    archivo.close()