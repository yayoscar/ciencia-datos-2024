idiomas = ['Ingles', 'Aleman', 'Español']
for idioma in idiomas:
    nombre_archivo = f"{idioma}.txt"
    with open(nombre_archivo, "w") as archivo:
        archivo.write(idioma)

        #for pais in paises:
        #archivo = open(f"{pais}.txt", "w")
        #archivo.write(pais)
        #archivo.close()
        #Comentario para ver como se hacia con open :)