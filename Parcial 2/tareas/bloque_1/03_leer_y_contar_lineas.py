with open("parrafo.txt", "r") as archivo:
  lineas = archivo.readlines()
  cantidad_lineas = len(lineas)
  print(f"El archivo tiene {cantidad_lineas} líneas.")