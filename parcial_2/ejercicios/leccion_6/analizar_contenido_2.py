with open("ensayo.txt", "r") as archivo:
    contenido = archivo.read()
    print(f"El archivo contiene {len(contenido)} caracteres.")
