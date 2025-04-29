try:
    with open("parrafo.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        numero_de_lineas = len(lineas)
        print(f"El archivo tiene {numero_de_lineas} líneas.")
except FileNotFoundError:
    print("Error: El archivo 'parrafo.txt' no fue encontrado.")