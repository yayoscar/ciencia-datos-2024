paises = ["Albania", "Bélgica", "Canadá", "Dinamarca", "Etiopía", "Francia"]

for pais in paises:
    with open(f"{pais}.txt", 'w', encoding='utf-8') as archivo:
        archivo.write(pais)