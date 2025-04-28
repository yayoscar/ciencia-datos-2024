palabras = ["miku", "neru", "teto"]

for palabra in palabras:
    archivo = open(f"{palabra}.txt", "w")
    archivo.write(palabra)
    archivo.close()
