fecha = input("Ingresa la fecha: ")
calificacion = input("Calificación del día: ")
descripcion = input("Descripcion del día:\n")

with open(f"dias/{fecha}.txt","w") as archivo:
    archivo.write(calificacion+ 2*"\n")
    archivo.write(descripcion)