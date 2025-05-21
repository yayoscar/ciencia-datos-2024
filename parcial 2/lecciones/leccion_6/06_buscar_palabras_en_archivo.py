palabra = input("Escribe una palabra: ").lower()

with open("texto.txt", "r",encoding="utf-8") as archivo:
    contenido = archivo.read().lower()

apariciones = contenido.count(palabra)

print(f"La palabra aparece {apariciones} veces.")