deportes = ["futbol", "basketball", "beisbol"]
for deporte in deportes:
    archivo=open(f"{deporte}.txt","w")
    archivo.write(deporte)
    archivo.close()