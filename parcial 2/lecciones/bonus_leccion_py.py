nombres = ['Oscar','Xavyer','Estrella','Julio']
archivos = ['Oscar.txt','Xavyer.txt','Estrella.txt','julio.txt']

for nombre,archivo in zip(nombres,archivos):
    file = open(archivo,"a")
    file.write(nombre)
    file.close()