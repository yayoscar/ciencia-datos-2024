def verificador_longitud_contrasena(clave):
    if len(clave) >8:
        return True
    return False
print(verificador_longitud_contrasena("clave1245"))