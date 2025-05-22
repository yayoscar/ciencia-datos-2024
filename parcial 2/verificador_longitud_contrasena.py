def verificar_contrasena(clave):
    return len(clave) >= 8
print(verificar_contrasena("miclave"))        # False
print(verificar_contrasena("miclavegrande"))  # True
