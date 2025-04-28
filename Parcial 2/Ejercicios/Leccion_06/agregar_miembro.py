archivo = open('miembro.txt',"a")
nombre = input("Agregar nuevo miembro: ")
archivo.write(f"{nombre}")
archivo.close()