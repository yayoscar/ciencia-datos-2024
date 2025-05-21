idiomas = ['ingles', 'aleman', 'español']
for idioma in idiomas:
    with open(f"{idioma}.txt","w") as archivo:
        archivo.write(idioma)