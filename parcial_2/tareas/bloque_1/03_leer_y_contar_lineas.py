texto = """Holaaaaaaaaaaaaaaaaaaaaaaa
Sooooooooooooooooooooooooooooy
Daniiiiiiiiiiiiiiiiiiiiiiii
Baiiiiiiiiiiiiiiiiiii
Mundooooooooooo
Pyhooooooon"""
archivo = open("parrafo.txt", "w")
archivo.write(texto)
archivo.close()
archivo = open("parrafo.txt", "r")
lineas = archivo.readlines()
archivo.close()
print(f"El archivo tiene {len(lineas)} líneas.")