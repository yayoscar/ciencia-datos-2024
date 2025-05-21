with open("ensayo.txt", "r") as archivo:
    contenido = archivo.read()
    contenido_modificado = contenido.title()
    print(contenido_modificado)
