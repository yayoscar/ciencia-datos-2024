def verficador_temperatura(temperatura):
    if temperatura > 7:
        return "Cálido"
    else:
        return "Frío"

print(verficador_temperatura(4))