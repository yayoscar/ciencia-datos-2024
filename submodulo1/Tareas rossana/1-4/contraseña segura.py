def es_contraseña_segura(contraseña):
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_simbolo = False
    simbolos = "!@#$%^&*()_+-=[]{}|;:',.<>/?"

    if len(contraseña) < 8:
        return False

    for caracter in contraseña:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True
        elif caracter in simbolos:
            tiene_simbolo = True

    if tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_simbolo:
        return True
    else:
        return False

# Programa principal
contraseña = input("Ingrese una contraseña: ")

if es_contraseña_segura(contraseña):
    print("La contraseña es segura.")
else:
    print("La contraseña no es segura.")
