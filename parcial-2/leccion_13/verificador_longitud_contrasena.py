def verificador_contraseña (clave):
    if len(clave)>=8:
        return True
    return False

print(verificador_contraseña("clave123456"))