def contrasena(clave):
    if len(clave) >= 8:
        return True
    return False

print(contrasena("yazuri123"))