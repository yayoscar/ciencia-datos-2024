nombres = ['Yarely','Lizeth','Genesis','Sherlin']
archivos = ['yarely.txt','lizeth.txt','genesis.txt','sherlin.txt']

for nombre,archivo in zip(nombres,archivos):
    file = open(archivo,"w")
    file.write(nombre)
    file.close()