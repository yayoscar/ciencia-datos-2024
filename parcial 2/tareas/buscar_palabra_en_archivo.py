palabra = input("Escribe la palabra a buscar: ")
archivo = open("texto.txt", "r")
texto = archivo.read().lower()
archivo.close()

busqueda = palabra.lower()
contador = 0
for i in range(len(texto) - len(busqueda) + 1):
    if texto[i:i+len(busqueda)] == busqueda:
        contador += 1

print(f"La palabra aparece {contador} veces.")
