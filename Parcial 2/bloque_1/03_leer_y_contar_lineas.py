def texto():
    texto = "Quiero ir a la playa y ver el mar y la arena.\nEl mar en el atardecer se ve increíble.\nLa brisa de el mar es refrescante."
    with open("párrafo.txt", "w") as archivo:
        archivo.write(texto)

def contar_lineas():
    with open("párrafo.txt", "r") as archivo:
        lineas = archivo.readlines()
        return len(lineas)

def main():
    texto()
    num_lineas = contar_lineas()
    print(f"El archivo 'párrafo.txt' tiene {num_lineas} líneas.")

