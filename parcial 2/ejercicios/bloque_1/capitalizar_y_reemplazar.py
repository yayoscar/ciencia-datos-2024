print("ola profe")
def capitaliza_y_reemplaza():
    frase = input("ingrese una frase: ")
    frase = frase.replace(" ","_")
    frase = frase.title()
    print(frase)
capitaliza_y_reemplaza()