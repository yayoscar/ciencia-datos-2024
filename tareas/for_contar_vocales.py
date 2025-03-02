palabras = ["hola", "mundo", "python", "programacion"]
vocales = "aeiou"

for palabra in palabras:
    contador_vocales = {vocal: palabra.count(vocal) for vocal in vocales}
    print(f"{palabra} tiene las siguientes vocales:")
    for vocal, cuenta in contador_vocales.items():
        print(f"  {vocal}: {cuenta}")

