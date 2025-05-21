def verificar_contraseña(contraseña):
    tiene_mayuscula = any(c.isupper() for c in contraseña)
    tiene_digito = any(c.isdigit() for c in contraseña)
    longitud_valida = len(contraseña) >= 8

    if tiene_mayuscula and tiene_digito and longitud_valida:
        return "Contraseña fuerte"
    else:
        return "contraseña debil"
