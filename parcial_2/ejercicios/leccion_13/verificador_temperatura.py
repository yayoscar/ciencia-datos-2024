def verificador_temperatura(temperatura):
    if temperatura < 7:
        return "frio"
    return "caliente"
print(verificador_temperatura(4))