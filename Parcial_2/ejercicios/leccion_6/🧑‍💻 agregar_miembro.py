
nuevo_miembro = input("Agregar nuevo miembro: ")

with open("miembros.txt", "w") as archivo:
    archivo.write(f"\n{nuevo_miembro}")


print("\nContenido actualizado del archivo:")
with open("miembros.txt", "r", ) as archivo:
    print(archivo.read())
