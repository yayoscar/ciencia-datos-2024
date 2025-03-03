palabras = ["hola","mundo","phyton", "programacion"]
vocales = "aeiou"
for palabra in palabras:
    contador = sum(palabra.count(vocales) for vocales in vocales)
    print(contador)