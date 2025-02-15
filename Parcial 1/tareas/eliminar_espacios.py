def eliminador_espacios():
    print("Bienvenido al eliminador de espacios extra.")
    texto = input("Por favor, ingresa una frase con espacios extra al inicio y al final: ")

    texto_limpio = texto.strip()

    print(f"Frase sin espacios extra: '{texto_limpio}'")


eliminador_espacios()
