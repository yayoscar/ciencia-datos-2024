def contar_caracteres():
    frases = ["hola mundo", "python es divertido", "vamos a practicar"]

    for index, frase in enumerate(frases):
        longitud = len(frase)  # Contar los caracteres de cada frase
        print(f"{index}: {frase} ({longitud} caracteres)")

# Ejecutar la función
contar_caracteres()
