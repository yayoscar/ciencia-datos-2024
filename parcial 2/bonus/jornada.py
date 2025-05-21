feacha=input("ingresa la fecha: ")
calificacion=int(input("calificacion del dia: "))
descripcion=input("descripcion del dia: ")

with open (f"dias/{fecha}.txt,","w") as archivo:
    archivo.write(calificacion)
    archivo.write(descripcion)

