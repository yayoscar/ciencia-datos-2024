with open ('parrafo.txt', 'w', encoding= 'utf-8') as archivo:
    archivo.write("Esta es la primera línea. \n")
    archivo.write("Aqui tenemos la segunda linea. \n")
    archivo.write("Y finalmente la tercera linea.\n")

with open('parrafo.txt', 'r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()
    cantidad = len(lineas)

print(f"EL ARCHIVO TIENE {cantidad} LINEAS")
