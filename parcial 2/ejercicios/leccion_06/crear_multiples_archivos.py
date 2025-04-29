paises= ["Albania","Belgica","Canada","Dinamarca","Etiopia","Francia"]


for pais in paises:
    archivo=open(f"{pais}.txt,""w")
    archivo.write(pais)
    archivo.close()