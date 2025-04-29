def lista():
    palabras = ["arena", "mar", "flores"]
    for palabra in palabras:
        with open(f"{palabra}.txt", "w") as archivo:
            archivo.write(palabra)
        print(f"Archivo {palabra}.txt creado")
