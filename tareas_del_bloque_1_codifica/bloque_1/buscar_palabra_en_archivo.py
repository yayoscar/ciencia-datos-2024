palabra = input("Ingrese una palabra: ").lower()

contador = 0

try:
    with open("texto.txt", "r") as archivo:
        for linea in archivo:
            palabras = linea.lower().split()
            contador += palabras.count(palabra)
except FileNotFoundError:
    print("El archivo texto.txt no existe.")
else:
    # Imprimir el resultado
    print(f"La palabra '{palabra}' aparece {contador} veces.")






