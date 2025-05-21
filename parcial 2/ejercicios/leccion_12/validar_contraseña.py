def fuerza(contraseña):
    tiene_mayuscula = False
    tiene_digito = False

    for c in contraseña:
        if c.isupper():
            tiene_mayuscula = True
        if c.isdigit():
            tiene_digito = True

    if len(contraseña) >= 8 and tiene_mayuscula and tiene_digito:
        return "contraseña Fuerte"
    else:
        return "Contraseña Débil"


print(fuerza("nwqbwhqvwfvñwS#"))