nombres = ['oscar', 'javier', 'estrella', 'julio']
archivos = ['oscar.txt', 'javier.txt', 'estrella.txt', 'julio.txt']

for nombre,archivo in zip(nombres, archivos):
    file = open(archivo, "w")
    file.write(nombre)
    file.close()