def verificar_longitud_contrasena(clave):
    if len(clave) >=8:
        return False

print(verificar_longitud_contrasena("clave12345678"))