def leer_y_contar_lineas():
    with (open("parrafo.txt","w") as archivo):
        archivo.write("esta es la primera linea.\n")
        archivo.write("esta es la segunda linea.\n")
        archivo.write("esta es la tercera linea.\n")

    with open("parrafo.txt","r") as archivo:
            lineas = archivo.readlines()
            print(f"el archivo tiene{len(lineas)} lineas.")
leer_y_contar_lineas()