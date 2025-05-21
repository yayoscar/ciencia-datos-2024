palabra = input("Ingrese una palabra: ").lower()
with open("texto.txt", "r") as archivo:
    texto = archivo.read().lower()
    texto = texto.count(palabra)
    print(f"La palabra {palabra} aparece {texto} veces en el archivo")
