def crear_archivos_desde_lista():
    palabras = ["ana","lisa","melano"]
    for palabra in palabras:
        with open(f"{palabra}.txt", "w") as archivo:
            archivo.write(palabra)
crear_archivos_desde_lista()