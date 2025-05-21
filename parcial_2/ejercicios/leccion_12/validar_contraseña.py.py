def fuerza(contraseña):
    if len(contraseña) < 8:
        return "Contraseña Débil"
    if not any(c.isupper() for c in contraseña):
        return "Contraseña Débil"
    if not any(c.isdigit() for c in contraseña):
        return "Contraseña Débil"
    return "Contraseña Fuerte"