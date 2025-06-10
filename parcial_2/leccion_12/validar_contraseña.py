def fuerza(contrasena):
    tiene_longitud = len(contrasena) >= 8
    tiene_mayuscula = any(c.isupper() for c in contrasena)
    tiene_digito = any(c.isdigit() for c in contrasena)

    if tiene_longitud and tiene_mayuscula and tiene_digito:
        return "Contraseña Fuerte"
    else:
        return "Contraseña Débil"