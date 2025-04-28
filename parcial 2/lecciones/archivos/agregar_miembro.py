archivo = open("miembros.txt", "a")
nombre = input("agregar un nuevo miembro: ")
archivo.write(f"{nombre}/n")
archivo.close()