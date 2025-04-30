paises=["albania", "belgica", "canada", "dinamarca", "etiopia", "francia"]

for pais in paises:
    archivo=open(f"{pais}.txt", "w")
    archivo.write(pais)
    archivo.close()
