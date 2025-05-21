def fuerza(contraseña):
    if len(contraseña) >= 8 and any(c.isupper() for c in contraseña) and any(c.isdigit() for c in contraseña):
        return "Contraseña Fuerte"
    return "Contraseña Débil"

print(fuerza("MiClave123"))  
print(fuerza("clave"))
