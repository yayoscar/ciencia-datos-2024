palabras=["caldo","sopa","mole"]
for palabra in palabras:
    archivo=open(f"{palabra}.txt","w" )
    archivo.write(palabra)
    archivo.close()

