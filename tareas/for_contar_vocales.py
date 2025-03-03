palabras = ["hola","mundo","python","programacion"]
vacales = "aeiou"
for palabra in palabras:
    contador = sum(palabra.lower().count(v) for v in vacales)
    print(f"{palabra}:{contador} vocales")