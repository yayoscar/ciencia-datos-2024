def longitud_contraseña(contraseña):
    if len(contraseña) >=8:
        return True
    return False


print(longitud_contraseña('clave12345678'))