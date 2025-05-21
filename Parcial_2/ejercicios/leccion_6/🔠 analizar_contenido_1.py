with open("ensayo.txt","r") as archivo:
    contenido=archivo.read()
    print(contenido)
    print(contenido.__len__())
