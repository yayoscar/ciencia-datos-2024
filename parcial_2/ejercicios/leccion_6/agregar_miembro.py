nuemiembro = input("Ingrese un nuevo miembro del equipo: ")
archivo = open("miembros.txt", "a")
archivo.write(nuemiembro)
archivo.close()