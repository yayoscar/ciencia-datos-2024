def fuerza(contraseña):
    if len(contraseña) <8:
        return "contraseña debil"

    tiene_mayuscula = any(c.isupper() for c in contraseña)
    tiene_digito = any(c.isdigit() for c in contraseña)

    if tiene_mayuscula and tiene_digito:
        return "contraseña fuerte"
    else:
        return "contraseña debil"
