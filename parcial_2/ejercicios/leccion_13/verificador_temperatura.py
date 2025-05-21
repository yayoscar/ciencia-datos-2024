def verificador_temperatura(temperatura):
    if temperatura > 7:
        return "Cálido"
    else:
        return "Frío"

print(verificador_temperatura(8))