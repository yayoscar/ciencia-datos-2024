palabras = ["z", "x","d"]
for palabras in palabras:
    archivo = open(f"{palabras}.txt", "w")
    archivo.write(palabras)