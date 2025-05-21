def fuerza(contraseña):
    longitud_valida = len(contraseña) >= 8
    tiene_mayuscula = any(c.isupper() for c in contraseña)
    tiene_digito = any(c.isdigit() for c in contraseña)
    if longitud_valida and tiene_mayuscula and tiene_digito:
        return "Contraseña Fuerte"
    else:
        return "Contraseña Débil"


print(fuerza("Pochacco05"))
