palabras = ["sol", "Luna", "estrella"]

for palabra in palabras:
    with open(f"{palabra}.txt", "w") as archivo:
        archivo.write(palabra)