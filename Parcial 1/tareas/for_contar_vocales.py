# Lista de palabras
palabras = ["hola", "mundo", "python", "programa", "vocales"]

# Definir una función para contar las vocales
def contar_vocales(palabra):
    # Definir las vocales
    vocales = "aeiou"
    contador = 0
    # Recorrer cada letra de la palabra
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador

# Recorrer la lista de palabras y contar las vocales
for palabra in palabras:
    print(f"La palabra '{palabra}' tiene {contar_vocales(palabra)} vocales.")
