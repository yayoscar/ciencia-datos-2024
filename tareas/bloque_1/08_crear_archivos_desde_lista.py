palabras = ["lapiz", "borrador", "tajador"]

for palabra in palabras:
    with open(f"{palabra}.txt", "w", encoding="utf-8") as archivo:
        archivo.write(palabra)

print("Archivos creados con éxito.")