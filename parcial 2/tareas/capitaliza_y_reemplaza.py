frase = input("Escribe una frase: ")
frase_guiones = frase.replace(" ", "_")

resultado = ""
palabra = ""
for caracter in frase_guiones:
    if caracter == "_":
        resultado += palabra.capitalize() + "_"
        palabra = ""
    else:
        palabra += caracter

resultado += palabra.capitalize()
print(resultado)
