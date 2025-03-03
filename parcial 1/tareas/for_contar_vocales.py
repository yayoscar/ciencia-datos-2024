palabras = ["hola", "mundo", "phyton", "programacion"]
vocales = "aeiuo"
for palabra in palabras:
    contador = sum(palabra.count(vocales) for vocales in vocales )
    print(contador)