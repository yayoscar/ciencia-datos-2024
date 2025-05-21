'''archivo = open('archivo.txt', 'w')
archivo.write('caracol')
archivo.close()'''
with open('caracol.txt', 'w') as archivo:
    archivo.write("caracol")