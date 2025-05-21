nombres=['Oscar', 'Xavier', 'Estrella', 'Julio']
archivos = ['oscar.txt', 'xavier.txt', 'estrella.txt', 'julio.txt']

for nombre,archivo in zip(nombres,archivos):
    file = open(archivo, "w")
    file.write(nombre)
    file.close()