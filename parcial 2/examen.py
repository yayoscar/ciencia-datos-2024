temperaturas = float(input("ingrese promedio de temperaturas:  "))
with "temperaturas":

    t1 = temperaturas.maxima
    t2 = temperaturas.minima
    print("temperatura maxima:",t1 )
    print("temperatura minima: ",t2 )


archivo = open("reporte_temperaturas.txt","r")
temperaturas = ("promedio:",18.8 )
maxima = ("maxima",22.7)
minima = ("minima", 15.3)
contenido = archivo.read()
print(contenido)