frase = input("Por favor, escribe una frase: ")
frase_modificada = '_'.join([palabra.capitalize() for palabra in frase.split()])
print("Frase modificada:", frase_modificada)
