fecha = input("ingresa la fecha: ")
calificacion = int(input("calificacion del dia: "))
descripcion = input("descripcion del dia:\n")

with open(f"dias/{fecha}.txt","w") as archivo:
    archivo.write(calificacion*"\n\n")
    archivo.write(descripcion)