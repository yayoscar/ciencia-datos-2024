paises = ["Albania","Bélgica","Canada","Dinamarca","Etiopía","Francia"]
for pais in paises:
    archivo = open(f"{pais}.txt","w")
    archivo.write(pais)
    archivo.close()