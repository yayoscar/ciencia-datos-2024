palabras = ["manzana", "fresa", "uva"]
for palabra in palabras:
  with open(f"{palabra}.txt", "w") as archivo:
    archivo.write(palabra)