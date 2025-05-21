def verificador_longitud_contraseña(clave):
    if len(clave) >=8:
        return True
    return False

print(verificador_longitud_contraseña("clave12345678"))