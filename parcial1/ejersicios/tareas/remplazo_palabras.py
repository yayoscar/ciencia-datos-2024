frase = input("ingresa una frase: ")
while True:
    cambio = input("indica que palabras deseas remplazar: ")
    remplazo = input("indica por cual palabra lo deseas remplazar: ")
    frase = frase.replace(cambio, remplazo)
    print("frase modificada:",frase)
