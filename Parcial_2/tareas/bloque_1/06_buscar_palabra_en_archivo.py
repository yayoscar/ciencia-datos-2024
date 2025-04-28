
palabra = input("Escribe una palabra: ")
archivo = open("texto.rtf.", "r")
contenido = archivo.read()
archivo.close()
contador = contenido.count(palabra)
print(f"La palabra aparece {contador} veces.")

