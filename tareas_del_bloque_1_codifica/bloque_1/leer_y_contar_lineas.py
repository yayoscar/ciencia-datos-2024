with open("parrafo.txt", "r", encoding="utf-8") as archivo:
    lineas = [linea for linea in archivo if linea.strip() != ""]

cantidad_lineas = len(lineas)
print(f"El archivo tiene {cantidad_lineas} líneas.")

