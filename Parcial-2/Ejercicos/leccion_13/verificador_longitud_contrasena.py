def verificador_contrasena(clave):
    if len(clave) >= 8:
        return True
    return False
print(verificador_contrasena("contrasena"))