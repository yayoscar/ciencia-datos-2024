paises=['Albania','Bélgica','Canadá','Dinamarca','Etiopía','Francia']
nombre_archivo=['ap.txt','bp.txt','cp.txt','dp.txt','ep.txt','fp.txt']
for pais,nombre_archivo in zip(paises,nombre_archivo):
    archivo=open(nombre_archivo,'w')
    archivo.write(pais)
    archivo.close()