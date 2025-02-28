palabras = ["hola", "mundo", "python", "programacion"]
vocales = "aeiou"
for palabra in palabras:
    contador = sum(palabra.lower().count(v) for v in vocales)
    print(f"{palabra}: {contador} vocales")