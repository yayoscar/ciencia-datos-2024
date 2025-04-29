paises = ["Albania", "Belgica", "Canada", "Dinamarca", "Etiopia"]
for pais in paises:
    archivo = open(f"{pais},txt","w")
    archivo.write(pais)
    archivo.close()