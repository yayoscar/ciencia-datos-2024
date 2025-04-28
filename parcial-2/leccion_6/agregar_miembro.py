archivo = open("miembros.txt", "a")
nombre=input("Agregue un nuevo miembro: ")
archivo.write(f"{nombre}\n")
archivo.close()