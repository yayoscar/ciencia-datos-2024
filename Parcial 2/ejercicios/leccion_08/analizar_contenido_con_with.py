with open('oso.txt', 'r') as archivo:
    contenido = archivo.read()
    num_caracteres = len(contenido)
    print(num_caracteres)