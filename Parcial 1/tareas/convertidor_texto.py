def convertidor_texto():
    print("Bienvenido al convertidor de texto.")
    texto = input("Por favor, ingresa una frase: ")

    print(f"Texto en minúsculas: {texto.lower()}")
    print(f"Texto en mayúsculas: {texto.upper()}")
    print(f"Texto con la primera letra en mayúscula: {texto.capitalize()}")


convertidor_texto()
