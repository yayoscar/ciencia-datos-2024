lista=[1.3,1.2,3.1,2.3,4.3]
lista.sort()
archivo = open('orden.txt', 'w')
for lis in lista:
    archivo.write(f"{lis}\n")
archivo.close()

