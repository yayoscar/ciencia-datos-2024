flores = ["tulipan","girasoles","margaritas"]
for flor in flores:
    archivo = open(f"{flor}.txt","w")
    archivo.write(flor)
    archivo.close()