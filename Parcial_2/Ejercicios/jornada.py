fecha = input("ingresa la fecha: ")
calificacion = input("calificacion del dia: ")
descrpcion = input("descrpcion del dia: \n")

with open(f"dias/{fecha}.txt","w") as archivo:
    archivo.write(calificacion+"\n")
    archivo.write(descrpcion)
