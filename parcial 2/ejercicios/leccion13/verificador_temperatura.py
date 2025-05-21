def verificador_temperatura(temperatura):
    if temperatura > 7:
        return "caliente"
    else:
        return "frio"


print(verificador_temperatura("8"))