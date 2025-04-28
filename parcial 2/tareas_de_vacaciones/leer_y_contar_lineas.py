f = open("parrafo.txt", "w")
f.write("Hola.\n")
f.write("Esto es una prueba.\n")
f.write("Tiene tres líneas.\n")
f.close()

f = open("parrafo.txt", "r")
lineas = f.readlines()
f.close()

print("El archivo tiene", len(lineas), "líneas.")