archivo = open("miembros.txt","a")
nombre = input("agregar nuevos miembros:")
archivo.write(f"{nombre}\n")
archivo.close()