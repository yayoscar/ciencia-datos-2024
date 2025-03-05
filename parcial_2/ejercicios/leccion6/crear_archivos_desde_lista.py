palabras=["pipshash","posole","rellenonegro"]
for palabra in palabras:
    archivo=open(f"{palabra}.txt","w" )
    archivo.write(palabra)
    archivo.close()