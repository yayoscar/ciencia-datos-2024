vocales= 'aeiouAEIOU'
palabras= ["hola", "mundo", "python", "programacion"]
for palabra in palabras:
    contador_vocales = 0
    for vocal in vocales:
        contador_vocales += palabra.count(vocal)
    print(f'La palabra "{palabra}" tiene {contador_vocales} vocales.')