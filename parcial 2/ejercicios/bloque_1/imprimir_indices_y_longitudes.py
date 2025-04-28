def imprimir_indices_y_longitudes():
    usuarios = ["juan perez", "maria lopez", "carlos nuñez"]
    frases = ["hola mundo", "java es mejor que python", "bañate cochino"]
    for i, frase in enumerate(frases):
        print(f"{i}: {frase} ({len(frase)} caracteres)")

imprimir_indices_y_longitudes()
