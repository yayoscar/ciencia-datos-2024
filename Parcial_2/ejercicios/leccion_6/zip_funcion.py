paises = ["Albania", "Bélgica", "Canadá", "Dinamarca", "Etiopía", "Francia"]
nombres_archivo = ["ap.txt", "bp.txt", "cp.txt", "dp.txt", "ep.txt", "fp.txt"]
for pais, archivo in zip(paises, nombres_archivo):
    with open(archivo, "w") as f:
        f.write(pais)
