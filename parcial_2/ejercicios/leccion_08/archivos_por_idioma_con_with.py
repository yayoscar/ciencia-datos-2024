idiomas = ['Ingles', 'Aleman', 'Español']
for idioma in idiomas:
    with open(f"{idioma}.txt","w") as archivo:
        archivo.write(idioma)