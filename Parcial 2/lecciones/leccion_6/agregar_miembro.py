archivo=open("miembros.txt", "a")
nombre= input("Agregar nuevo miembro")
archivo.write(f"{nombre}\n")
archivo.close()