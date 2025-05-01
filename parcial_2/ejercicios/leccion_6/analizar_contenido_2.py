archivo = open('ensayo.txt', 'r')
print(f"El archivo contiene {len(archivo.read())} caracteres.")
archivo.close()