palabras = ["hola", "mundo", "python", "programacion"]

vocales = "aeiouAEIOU"

for palabra in palabras:
    contador = sum(palabra.count(v) for v in vocales)
    print(f"La palabra '{palabra}' tiene {contador} vocales.")