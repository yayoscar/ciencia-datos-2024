nombres = ["oscar","xavier","estrella","julio"]
archivos = ["oscar.txt","xavier.txt","estrella.txt","julio.txt"]

for nombres,archivos in zip(nombres,archivos):
    file = open(archivos,"a")
    file.write(nombres)
    file.close()
