paises = ["Albania", "Bélgica", "Canadá", "Dinamarca", "Etiopía", "Francia"]
for pais in paises:
    with open(f"{pais}.txt", "w", ) as archivo:
        archivo.write(pais)
