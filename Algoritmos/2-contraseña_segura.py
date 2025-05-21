contraseña = input("Ingrese una contraseña: ")

mayuscula = False
numero = False

if len(contraseña) < 8:
    print("La contraseña debe tener más de 8 caracteres.")
else:
    for caracter in contraseña:
        if caracter.isupper():
            mayuscula = True
        elif caracter.isdigit():
            numero = True

    if not mayuscula:
        print("La contraseña debe tener al menos una letra mayúscula.")
    elif not numero:
        print("La contraseña debe tener al menos un número.")
    else:
        print("La contraseña es segura")
