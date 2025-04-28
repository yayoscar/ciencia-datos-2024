lista = ["dani", "lolo", "pacho"]

for palabra in lista:
    archivo = open(palabra + ".txt", "w")
    for letra in palabra:
        archivo.write(letra)
    archivo.close()
