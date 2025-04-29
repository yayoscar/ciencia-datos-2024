try:
    with open("texto.txt", "r") as archivo:
        texto = archivo.read()
        palabra = input("Introduce una palabra: ")
        cuenta = texto.lower().count(palabra.lower()) #case-insensitive count
        print(f"La palabra '{palabra}' aparece {cuenta} veces.")
except FileNotFoundError:
    print("El archivo 'texto.txt' no se encontró.")