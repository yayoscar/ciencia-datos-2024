nombres = ['oscar','xavier','estrella','julio']
archivo = ['oscar.txt','xavier.txt','estrella.txt','julio.txt']

for nombre,archivo in zip(nombres ,archivo):
    file = open(archivo,'w')
    file.write(nombre)
    file.close()