def verificador_de_contraseña(clave):
    if len(clave) < 8:
        return False
    return True
print(verificador_de_contraseña("cesar2228"))
