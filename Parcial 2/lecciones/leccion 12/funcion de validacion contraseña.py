def fuerza(contraseña):
    longitud_valida = len(contraseña) >= 8
    tiene_mayuscula = (caracter.isupper() for caracter in contraseña)
    tiene_digito = (caracter.isdigit() for caracter in contraseña)
    if longitud_valida and tiene_mayuscula and tiene_digito:
        return "Contraseña Fuerte"
    else:
        return "Contraseña débil"
contraseña1 = input("ingresa la contraseña: ")
print(f"{fuerza(contraseña1)}")