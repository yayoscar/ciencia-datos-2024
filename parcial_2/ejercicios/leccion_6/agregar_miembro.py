nuevo_miembro = input("Ingrese al nuevo miembro: ")
nuevo_miembro = f"{nuevo_miembro}\n"
archivo = open('miembros.txt', 'a')
archivo.write(nuevo_miembro)
archivo.close()
print(f"¡{nuevo_miembro} ha sido agregado a la lista!")