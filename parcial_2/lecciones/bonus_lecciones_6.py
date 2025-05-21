nombres = ["Oscar", "Xavier", "Estrella", "Julio"]
archivos = ["Oscar.txt", "Xavier.txt", "Estrella.txt", "Julio.txt"]

for nombre,archivo in zip(nombres, archivos):
    file = open(archivo, "w")
    file.write(nombre)
    file.close()