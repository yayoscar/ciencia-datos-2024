def verificador_temperatura(temperatura):
    if temperatura > 7:
        return "Calido"
    else:
        return "Frio"

print(verificador_temperatura(8))
