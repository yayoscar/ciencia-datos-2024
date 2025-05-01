archivo = open('ensayo.txt', 'r')
letras = archivo.read()
print(letras.title())
archivo.close()