
archivo = open(r"C:\Users\omary\Downloads\archivos leccion 6\ensayo.txt", 'r')


contenido = archivo.read()


archivo.close()

numero_de_caracteres = len(contenido)
print(f"El archivo contiene {numero_de_caracteres} caracteres.")