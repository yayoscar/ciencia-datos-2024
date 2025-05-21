palabra = input("Escribela palabra que quieres buscar:")
with open("texto.txt", "r") as archivo:
    contenido = archivo.read( )
    cantidad = contenido.lower().count(palabra.lower())
print(f"la palabra aparece {cantidad} veces.")
