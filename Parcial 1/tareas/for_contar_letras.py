def contar_letras_palabras():
    print("Bienvenido al contador de letras en palabras.")
    palabras = ["gato", "elefante", "casa", "montaña", "avión"]

    print("Cantidad de letras en cada palabra:")
    for palabra in palabras:
        print(f"{palabra}: {len(palabra)} letras")


contar_letras_palabras()
