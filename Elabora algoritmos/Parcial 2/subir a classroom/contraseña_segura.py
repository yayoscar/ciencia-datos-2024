def es_contraseña_segura(contraseña):
    if len(contraseña) <= 8:
        return False

    tiene_mayuscula = False
    tiene_numero = False

    for c in contraseña:
        if c.isupper():
            tiene_mayuscula = True
        if c.isdigit():
            tiene_numero = True

    return tiene_mayuscula and tiene_numero

contraseña = input("Ingresa una contraseña: ")

if es_contraseña_segura(contraseña):
    print("La contraseña es segura.")
else:
    print("La contraseña NO es segura.")
