
with open("texto.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read().lower()
palabra = input("Escribe una palabra para buscar: ").lower()
cantidad = contenido.count(palabra)

print(f"La palabra aparece {cantidad} veces.")
