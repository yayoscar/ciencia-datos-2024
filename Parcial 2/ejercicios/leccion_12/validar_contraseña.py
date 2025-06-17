def fuerza(contraseña):
    longitud_valida = len(contraseña) >= 8
    mayusculas = any(c.isupper() for c in contraseña)
    digito = any(c.isdigit() for c in contraseña)

    if longitud_valida and mayusculas and digito:
        return "Contraseña fuerte."
    else:
        return "Contraseña débil."

contraseña = input("Ingrese una contraseña: ")
print(fuerza(contraseña))