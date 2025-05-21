def verificar_temperatura(temperatura):
    if temperatura > 7:
        return "calido"
    else:
        return "frio"


print(verificar_temperatura(8))