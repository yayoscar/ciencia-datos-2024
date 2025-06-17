archivo = open("miembros.txt", "a")
nuevo_miembro = input("Agregar nuevo miembro: ")
archivo.write("\n" + nuevo_miembro)
archivo.close()