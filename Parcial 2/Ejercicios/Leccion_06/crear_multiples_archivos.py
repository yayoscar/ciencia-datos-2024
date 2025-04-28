paises = ("Albania", "Bélgica", "Canadá", "Dinamarca", "Etiopía")

for país in paises:
    archivo = open(f"{país}.txt,w")
    archivo.write(país)
    archivo.close()