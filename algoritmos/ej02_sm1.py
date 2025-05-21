def es_contrasena_segura(contrasena):
    if len(contrasena) <= 8:
        return False

    tiene_mayuscula = False
    tiene_numero = False

    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True
        if caracter.isnumeric():
                tiene_numero = True

    return tiene_mayuscula and tiene_numero

def main():
    contrasena = input("Ingresa tu contraseña: ")
    if es_contrasena_segura(contrasena):
        print("La contraseña es segura.")
    else:
        print("La contraseña NO es segura. Debe tener más de 8 caracteres, al menos una letra mayuscula y al menos un número.")


if __name__ == "__main__":
    main()
