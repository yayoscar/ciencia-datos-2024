contenido = """Este es un ejemplo de texto.
yo solo se que no se nada."""
with open("texto.txt", "w") as archivo:
    archivo.write(contenido)
palabra = input("Introduce una palabra para buscar: ")
with open("texto.txt", "r") as archivo:
    texto = archivo.read()
contador = texto.lower().count(palabra.lower())
print(f"La palabra aparece {contador} veces.")