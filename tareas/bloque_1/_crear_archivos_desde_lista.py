palabras = ["manzana", "naranja", "mango"]

for palabra in palabras:
    with open(f"{palabra}.txt", "w") as archivo:

        archivo.write(palabra)

print("Los archivos han sido creados exitosamente.")
