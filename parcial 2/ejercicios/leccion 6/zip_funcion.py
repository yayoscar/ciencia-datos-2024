paises=["alabania","belgica","canada","dinamarca","etiopia","francia"]
nombres_archivos = ["ap.txt","bp.txt","cp.txt","dp.txt","ep.txt"]
for pais,nombres_archivos in zip(paises,nombres_archivos):
    archivo = open(nombres_archivos,"w")
    archivo.write(pais)
    archivo.close()