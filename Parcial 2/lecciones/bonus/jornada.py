fecha = input("Ingresa la fecha: ")
calificacion = input("Ingresa la calificacion del día: ")
descripcion = input("Descripción del día:\n")

with open(f"dias/{fecha}.txt", "w") as archivo:
    archivo.writelines(calificacion + 2 * "\n")
    archivo.write(descripcion)