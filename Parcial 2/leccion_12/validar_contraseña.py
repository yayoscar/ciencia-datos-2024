def fuerza(contraseña):
    condiciones = []
    if len(contraseña) >= 8:
        condiciones.append(True)
    else:
        condiciones.append(False)

    digito = False
    for letra in contraseña:
        if letra.isdigit():
            digito = True

    condiciones.append(digito)

    mayuscula = False
    for letra in contraseña:
        if letra.isupper():
            mayuscula = True

    condiciones.append(mayuscula)

    if all(condiciones):
        return ("Password Fuerte")
    else:
        return ("Password debil")

    
print(fuerza("MICLavees2356554"))