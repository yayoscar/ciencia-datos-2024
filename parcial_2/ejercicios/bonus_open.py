contenidos=["Oscar Perez Olan","Juan Pablo Canul Yeh","Jorge Luis Garcia"]
archivos=["oscar.txt","juan.txt","jorge.txt"]

for contenido,archivo in zip(contenidos,archivos):
    a = open(f"../archivos/{archivo}", 'w')
    a.write(contenido)