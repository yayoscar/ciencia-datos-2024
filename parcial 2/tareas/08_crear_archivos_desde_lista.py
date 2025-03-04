palabras = ["z", "x", "d"]

for palabra in palabras:
    archivo = open(f"{palabra}.txt", "w")
    archivo.write(palabra)
    archivo.close()
