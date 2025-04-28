archivo = open("miembros.txt", "a")
nombre = input("ingresa el nuevo miembro: ")
archivo.write(f"{nombre}\n")
archivo.close()
