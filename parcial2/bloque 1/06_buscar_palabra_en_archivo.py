archivo = open("texto", "r")
palabra = input("Introduce una palabra para buscar: ")

contenido = archivo.read()
contador = contenido.lower().count(palabra.lower())

print(f"La palabra aparece {contador} veces.")
archivo.close()