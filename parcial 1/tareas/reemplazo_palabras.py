frase = input("ingresa una frase: ")
while True:
    cambio = input("indica que palabra deseas reemplazar: ")
    reemplazo = input("indica por cual palabra lo deseas reemplazar: ")
    frase = frase.replace(cambio, reemplazo)
    print("frase modificada:", frase)
