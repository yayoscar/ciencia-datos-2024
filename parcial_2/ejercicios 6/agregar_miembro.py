archivo = open("miembros.txt","a")
nombre = input("agregar nuevo miembro: ")
archivo.write(f"{nombre}n")
archivo.close()