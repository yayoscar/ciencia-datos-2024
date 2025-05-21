paises =["albania","belgica","canada","dinamarca","etiopia","francia"]
nombres_archivos = ['ap.txt','bp.txt','cp.txt','dp.txt','ep.txt','fr.txt']
for pais,nombre_archivos in zip(paises,nombres_archivos):
    archivo = open(nombre_archivos,"w")
    archivo.write(pais)
    archivo.close()