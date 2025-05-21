paises = ["Albania", "Bélgica", "Canadá", "Dinamarca", "Etiopía", "Francia"]
nombres_archivo = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']
for pais,nombre in zip(paises, nombres_archivo):
    archivo = open(f"{nombre}.txt", "w")
    archivo.write(pais)
    archivo.close