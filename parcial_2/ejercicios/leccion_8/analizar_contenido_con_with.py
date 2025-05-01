'''archivo = open('ensayo.txt', 'r')
caract = len(archivo.read())
print(caract)
archivo.close()'''
with open('oso.txt', 'r') as archivo:
    caracteres = len(archivo.read())
print(caracteres)