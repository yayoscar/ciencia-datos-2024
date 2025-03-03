frase = input("ingresa una frase: ")
while True:
    cambio = input("indica la palabra que deseas remplazar: ")
    reemplazo = input("indica por cual palabra la deseas reemplazar: ")
    frase = frase.replace(cambio, reemplazo)
    print("frase modificada:", frase)
