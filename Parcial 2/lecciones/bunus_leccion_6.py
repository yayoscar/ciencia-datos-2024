nombres=['oscas','xavyer','estrella','julio']
archivos=['oscas.txt','xavyer txt','estrella txt','julio txt']
for nombre,archivo in zip(nombres,archivos):
    file = open(archivo,"w")
    file.write(nombre)
    file.close()