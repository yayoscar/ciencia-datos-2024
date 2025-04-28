frases = ["hola mundo", "python es divertido", "vamos a practicar"]

i = 0
while i < len(frases):
    frase = frases[i]
    longitud = 0
    for c in frase:
        longitud += 1
    print(f"{i}: {frase} ({longitud} caracteres)")
    i += 1
