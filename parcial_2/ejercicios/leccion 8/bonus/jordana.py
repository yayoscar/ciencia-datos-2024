fecha = input("Ingrese la fecha")
calificacion = input("ingrese la calificacion del dia: ")
descripcion = input("Ingrese la descripcion del dia: \n")

with open(f"dias/{fecha}.txt", "w") as archivo:
    archivo.write(calificacion+"\n\n")
    archivo.write(descripcion)