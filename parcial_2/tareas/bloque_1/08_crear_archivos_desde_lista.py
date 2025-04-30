palabras = ["manzana", "banana", "cereza"]
for palabra in palabras:
    archivo = open(f"{palabra}.txt", "w")
    archivo.write(palabra)
    archivo.close()