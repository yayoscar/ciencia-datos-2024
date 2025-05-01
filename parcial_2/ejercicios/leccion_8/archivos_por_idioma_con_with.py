idiomas = ['inglés', 'Alemán', 'Español']
for idioma in idiomas:
    with open(f"{idioma}.txt", "w") as archivo:
        archivo.write(idioma)
#Iterar es repetir