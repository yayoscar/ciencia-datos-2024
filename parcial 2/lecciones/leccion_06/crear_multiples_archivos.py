paises = ["albania", "belgica", "canada", "dinamarca", "etiopoia", "franciaa"]

for pais in paises:
    archivo = open(f"´{pais}.txt", "w")
    archivo.write(pais)
    archivo.close()