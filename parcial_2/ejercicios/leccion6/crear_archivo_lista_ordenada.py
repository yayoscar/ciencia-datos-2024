lista=[6.2,1.23,9.3,5.4,4.1]
lista.sort()
archivo = open('orden.txt', 'w')
for lis in lista:
    archivo.write(f"{lis}\n")
archivo.close()