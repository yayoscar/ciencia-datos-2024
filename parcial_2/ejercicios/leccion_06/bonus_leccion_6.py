nombres=['oscar','xavier','estrella']
archivos=['oscar.txt','xavier.txt','estrella.txt']
for nombre,archivo in zip(nombres,archivos):
    file= open(archivo,"w")
    file.write(nombre)
    file.close()
