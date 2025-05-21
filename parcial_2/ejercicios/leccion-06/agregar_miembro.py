archivo = open("miembros.txt", "a")
nombre = input("Agregar un nuevo miembro: ")
archivo.write(f"{nombre}\n")
archivo.close()