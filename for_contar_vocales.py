palabras = ["hola", "mundo", "python", "programacion"]
vocales = "aeiou"

for palabra in palabras:
    conteo_vocales = {vocal: palabra.count(vocal) for vocal in vocales}  # Crear un diccionario de conteo por vocal
    print(f"Para la palabra '{palabra}':")
    for vocal in vocales:  # Imprimir las vocales de la "a" a la "u"
        print(f"  {vocal.upper()}: {conteo_vocales[vocal]}")


