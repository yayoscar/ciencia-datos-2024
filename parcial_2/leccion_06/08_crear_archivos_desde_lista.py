palabras = ["hola", "mundo", "python"]

for palabra in palabras:
    f = open(palabra + ".txt", "w")
    f.write(palabra)
    f.close()