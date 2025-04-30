paises = ["Albania", "Bélgica", "Canadá", "Dinamarca", "Etiopía", "Francia"]
for pais in paises:
    archivo = open(f"{pais}.txt","w")
    archivo.write(pais)
    archivo.close()