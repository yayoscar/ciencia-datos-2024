paises = ["Albania", "Bélgica", "Canadá", "Dinamarca", "Etiopía", "Francia"]
for pais in paises:
    file = open(f'{pais}.txt', 'w')
    file.write(pais)
    file.close()