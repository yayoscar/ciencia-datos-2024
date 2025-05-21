paises = ["Albania", "Bélgica", "Canadá", "Dinamarca", "Etiopía", "Francia"]
nombres_archivo = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']

for nombre_archivo, pais in zip(nombres_archivo, paises):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(pais)
